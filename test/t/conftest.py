import difflib
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from enum import Enum
from pathlib import Path
from types import TracebackType
from typing import (
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
)

import pexpect  # type: ignore[import]
import pytest

PS1 = "/@"
MAGIC_MARK = "__MaGiC-maRKz-NEtXZVZfKC__"
MAGIC_MARK2 = "Re8SCgEdfN"


def find_unique_completion_pair(
    items: Iterable[str],
) -> Optional[Tuple[str, str]]:
    result = None
    bestscore = 0
    sitems = sorted(set(items))
    for i in range(len(sitems)):
        cur = sitems[i]
        curlen = len(cur)
        prv = sitems[i - 1] if i != 0 else ""
        prvlen = len(prv)
        nxt = sitems[i + 1] if i < len(sitems) - 1 else ""
        nxtlen = len(nxt)
        diffprv = prv == ""
        diffnxt = nxt == ""
        # Analyse each item of the list and look for the minimum length of the
        # partial prefix which is distinct from both nxt and prv. The list
        # is sorted so the prefix will be unique in the entire list.
        for j in range(curlen):
            curchar = cur[j]
            if not diffprv and (j >= prvlen or prv[j] != curchar):
                diffprv = True
            if not diffnxt and (j >= nxtlen or nxt[j] != curchar):
                diffnxt = True
            if diffprv and diffnxt:
                break
        # At the end of the loop, j is the index of last character of
        # the unique partial prefix. The length is one plus that.
        parlen = j + 1
        if parlen >= curlen:
            continue
        # Try to find the most "readable pair"; look for a long pair where
        # part is about half of full.
        if parlen < curlen / 2:
            parlen = int(curlen / 2)
        score = curlen - parlen
        if score > bestscore:
            bestscore = score
            result = (cur[:parlen], cur)
    return result


@pytest.fixture(scope="class")
def output_sort_uniq(bash: pexpect.spawn) -> Callable[[str], List[str]]:
    def _output_sort_uniq(command: str) -> List[str]:
        return sorted(
            set(  # weed out possible duplicates
                assert_bash_exec(bash, command, want_output=True).split()
            )
        )

    return _output_sort_uniq


@pytest.fixture(scope="class")
def part_full_user(
    bash: pexpect.spawn, output_sort_uniq: Callable[[str], List[str]]
) -> Optional[Tuple[str, str]]:
    res = output_sort_uniq("compgen -u")
    pair = find_unique_completion_pair(res)
    if not pair:
        pytest.skip("No suitable test user found")
    return pair


@pytest.fixture(scope="class")
def part_full_group(
    bash: pexpect.spawn, output_sort_uniq: Callable[[str], List[str]]
) -> Optional[Tuple[str, str]]:
    res = output_sort_uniq("compgen -g")
    pair = find_unique_completion_pair(res)
    if not pair:
        pytest.skip("No suitable test user found")
    return pair


@pytest.fixture(scope="class")
def hosts(bash: pexpect.spawn) -> List[str]:
    output = assert_bash_exec(bash, "compgen -A hostname", want_output=True)
    return sorted(set(output.split() + _avahi_hosts(bash)))


@pytest.fixture(scope="class")
def avahi_hosts(bash: pexpect.spawn) -> List[str]:
    return _avahi_hosts(bash)


def _avahi_hosts(bash: pexpect.spawn) -> List[str]:
    output = assert_bash_exec(
        bash,
        "! type avahi-browse &>/dev/null || "
        "avahi-browse -cpr _workstation._tcp 2>/dev/null "
        "| command grep ^= | cut -d';' -f7",
        want_output=None,
    )
    return sorted(set(output.split()))


@pytest.fixture(scope="class")
def known_hosts(bash: pexpect.spawn) -> List[str]:
    output = assert_bash_exec(
        bash,
        '_comp_compgen_known_hosts ""; '
        r'printf "%s\n" "${COMPREPLY[@]}"; unset -v COMPREPLY',
        want_output=True,
    )
    return sorted(set(output.split()))


@pytest.fixture(scope="class")
def user_home(bash: pexpect.spawn) -> Tuple[str, str]:
    user = assert_bash_exec(
        bash, 'id -un 2>/dev/null || echo "$USER"', want_output=True
    ).strip()
    # We used to echo $HOME here, but we expect that it will be consistent with
    # ~user as far as bash is concerned which may not hold.
    home = assert_bash_exec(bash, "echo ~%s" % user, want_output=True).strip()
    return (user, home)


def partialize(
    bash: pexpect.spawn, items: Iterable[str]
) -> Tuple[str, List[str]]:
    """
    Get list of items starting with the first char of first of items.

    Disregard items starting with a COMP_WORDBREAKS character
    (e.g. a colon ~ IPv6 address), they are special cases requiring
    special tests.
    """
    first_char = None
    comp_wordbreaks = assert_bash_exec(
        bash,
        'printf "%s" "$COMP_WORDBREAKS"',
        want_output=True,
        want_newline=False,
    )
    partial_items = []
    for item in sorted(items):
        if first_char is None:
            if item[0] not in comp_wordbreaks:
                first_char = item[0]
                partial_items.append(item)
        elif item.startswith(first_char):
            partial_items.append(item)
        else:
            break
    if first_char is None:
        pytest.skip("Could not generate partial items list from %s" % items)
        # superfluous/dead code to assist mypy; pytest.skip always raises
        assert first_char is not None
    return first_char, partial_items


@pytest.fixture(scope="class")
def bash(request) -> pexpect.spawn:
    logfile: Optional[TextIO] = None
    histfile = None
    tmpdir = None
    bash = None

    if os.environ.get("BASH_COMPLETION_TEST_LOGFILE"):
        logfile = open(os.environ["BASH_COMPLETION_TEST_LOGFILE"], "w")
    elif os.environ.get("CI"):
        logfile = sys.stdout

    testdir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)
    )

    # Create an empty temporary file for HISTFILE.
    #
    # To prevent the tested Bash processes from writing to the user's
    # history file or any other files, we prepare an empty temporary
    # file for each test.
    #
    # - Note that HISTFILE=/dev/null may not work.  It results in the
    #   removal of the device /dev/null and the creation of a regular
    #   file at /dev/null when the number of commands reach
    #   HISTFILESIZE due to a bug in bash 4.3.  This causes execution of
    #   garbage through BASH_COMPLETION_USER_FILE=/dev/null.
    # - Note also that "unset -v HISTFILE" in "test/config/bashrc" was not
    #   adopted because "test/config/bashrc" is loaded after the
    #   history is read from the history file.
    #
    histfile = tempfile.NamedTemporaryFile(
        prefix="bash-completion-test_", delete=False
    )

    try:
        # release the file handle so that Bash can open the file.
        histfile.close()

        env = os.environ.copy()
        env.update(
            dict(
                SRCDIR=testdir,  # TODO needed at least by bashrc
                SRCDIRABS=testdir,
                PS1=PS1,
                INPUTRC="%s/config/inputrc" % testdir,
                TERM="dumb",
                LC_COLLATE="C",  # to match Python's default locale unaware sort
                HISTFILE=histfile.name,
            )
        )

        marker = request.node.get_closest_marker("bashcomp")

        # Set up the current working directory
        cwd = None
        if marker:
            if "cwd" in marker.kwargs and marker.kwargs.get("cwd") is not None:
                cwd = os.path.join(
                    testdir, "fixtures", marker.kwargs.get("cwd")
                )
            elif "temp_cwd" in marker.kwargs and marker.kwargs.get("temp_cwd"):
                tmpdir = tempfile.TemporaryDirectory(
                    prefix="bash-completion-test_"
                )
                cwd = tmpdir.name
        if cwd is None:
            cwd = os.path.join(testdir, "fixtures")
        os.chdir(cwd)

        # Start bash
        bash = pexpect.spawn(
            "%s --norc" % os.environ.get("BASH_COMPLETION_TEST_BASH", "bash"),
            maxread=os.environ.get(
                "BASH_COMPLETION_TEST_PEXPECT_MAXREAD", 20000
            ),
            logfile=logfile,
            cwd=cwd,
            env=env,
            encoding="utf-8",  # TODO? or native or...?
            # FIXME: Tests shouldn't depend on dimensions, but it's difficult to
            # expect robustly enough for Bash to wrap lines anywhere (e.g. inside
            # MAGIC_MARK).  Increase window width to reduce wrapping.
            dimensions=(24, 240),
            # TODO? codec_errors="replace",
        )
        bash.expect_exact(PS1)

        # Load bashrc and bash_completion
        bash_completion = os.environ.get(
            "BASH_COMPLETION_TEST_BASH_COMPLETION",
            "%s/../bash_completion" % testdir,
        )
        assert_bash_exec(bash, "source '%s/config/bashrc'" % testdir)
        assert_bash_exec(bash, "source '%s'" % bash_completion)

        # Use command name from marker if set, or grab from test filename
        cmd = None  # type: Optional[str]
        cmd_found = False
        if marker:
            cmd = marker.kwargs.get("cmd")
            cmd_found = "cmd" in marker.kwargs
            # Run pre-test commands, early so they're usable in skipif
            for pre_cmd in marker.kwargs.get("pre_cmds", []):
                assert_bash_exec(bash, pre_cmd, want_output=None)
            # Process skip and xfail conditions
            skipif = marker.kwargs.get("skipif")
            if skipif:
                try:
                    assert_bash_exec(bash, skipif, want_output=None)
                except AssertionError:
                    pass
                else:
                    bash.close()
                    bash = None
                    pytest.skip(skipif)
            xfail = marker.kwargs.get("xfail")
            if xfail:
                try:
                    assert_bash_exec(bash, xfail, want_output=None)
                except AssertionError:
                    pass
                else:
                    pytest.xfail(xfail)
        if not cmd_found:
            match = re.search(
                r"^test_(.+)\.py$", os.path.basename(str(request.fspath))
            )
            if match:
                cmd = match.group(1)
        if (
            marker
            and marker.kwargs
            and marker.kwargs.get("require_cmd", False)
        ):
            if not is_bash_type(bash, cmd):
                pytest.skip("Command not found")

        request.cls.cmd = cmd

        if (cmd_found and cmd is None) or is_testable(bash, cmd):
            before_env = get_env(bash)
            yield bash
            # Not exactly sure why, but some errors leave bash in state where
            # getting the env here would fail and trash our test output. So
            # reset to a good state first (Ctrl+C, expect prompt).
            bash.sendintr()
            bash.expect_exact(PS1)
            diff_env(
                before_env,
                get_env(bash),
                marker.kwargs.get("ignore_env") if marker else "",
            )

        if marker:
            for post_cmd in marker.kwargs.get("post_cmds", []):
                assert_bash_exec(bash, post_cmd, want_output=None)

    finally:
        # Clean up
        if bash:
            bash.close()
        if tmpdir:
            tmpdir.cleanup()
        if histfile:
            try:
                os.remove(histfile.name)
            except OSError:
                pass
        if logfile and logfile != sys.stdout:
            logfile.close()


def is_testable(bash: pexpect.spawn, cmd: Optional[str]) -> bool:
    if not cmd:
        pytest.fail("Could not resolve name of command to test")
        return False
    if not load_completion_for(bash, cmd):
        pytest.skip("No completion for command %s" % cmd)
    return True


def is_bash_type(bash: pexpect.spawn, cmd: Optional[str]) -> bool:
    if not cmd:
        return False
    typecmd = "type %s &>/dev/null && echo -n 0 || echo -n 1" % cmd
    bash.sendline(typecmd)
    bash.expect_exact(typecmd + "\r\n")
    result = bash.expect_exact(["0", "1"]) == 0
    bash.expect_exact(PS1)
    return result


def load_completion_for(bash: pexpect.spawn, cmd: str) -> bool:
    try:
        # Allow _comp_load to fail so we can test completions
        # that are directly loaded in bash_completion without a separate file.
        assert_bash_exec(bash, "_comp_load -- %s || :" % cmd)
        assert_bash_exec(bash, "complete -p -- %s &>/dev/null" % cmd)
    except AssertionError:
        return False
    return True


def assert_bash_exec(
    bash: pexpect.spawn,
    cmd: str,
    want_output: Optional[bool] = False,
    want_newline=True,
) -> str:
    """
    :param want_output: if None, don't care if got output or not
    """

    # Send command
    bash.sendline(cmd)
    bash.expect_exact(cmd)

    # Find prompt, output is before it
    bash.expect_exact("%s%s" % ("\r\n" if want_newline else "", PS1))
    output = bash.before

    # Retrieve exit status
    echo = "echo $?"
    bash.sendline(echo)
    got = bash.expect(
        [
            r"^%s\r\n(\d+)\r\n%s" % (re.escape(echo), re.escape(PS1)),
            PS1,
            pexpect.EOF,
            pexpect.TIMEOUT,
        ]
    )
    status = bash.match.group(1) if got == 0 else "unknown"

    assert status == "0", 'Error running "%s": exit status=%s, output="%s"' % (
        cmd,
        status,
        output,
    )
    if want_output is not None:
        if output:
            assert want_output, (
                'Unexpected output from "%s": exit status=%s, output="%s"'
                % (
                    cmd,
                    status,
                    output,
                )
            )
        else:
            assert not want_output, (
                'Expected output from "%s": exit status=%s, output="%s"'
                % (
                    cmd,
                    status,
                    output,
                )
            )

    return output


class bash_env_saved:
    counter: int = 0

    class saved_state(Enum):
        ChangesDetected = 1
        ChangesIgnored = 2

    def __init__(self, bash: pexpect.spawn, sendintr: bool = False):
        bash_env_saved.counter += 1
        self.prefix: str = "_comp__test_%d" % bash_env_saved.counter

        self.bash = bash
        self.cwd_changed: bool = False
        self.saved_set: Dict[str, bash_env_saved.saved_state] = {}
        self.saved_shopt: Dict[str, bash_env_saved.saved_state] = {}
        self.saved_variables: Dict[str, bash_env_saved.saved_state] = {}
        self.sendintr = sendintr

        self.noexcept: bool = False
        self.captured_error: Optional[Exception] = None

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType],
    ) -> None:
        self._restore_env()
        return None

    def _safe_sendintr(self):
        try:
            self.bash.sendintr()
            self.bash.expect_exact(PS1)
        except Exception as e:
            if self.noexcept:
                self.captured_error = e
            else:
                raise

    def _safe_exec(self, cmd: str):
        try:
            self.bash.sendline(cmd)
            self.bash.expect_exact(cmd)
            self.bash.expect_exact("\r\n" + PS1)
        except Exception as e:
            if self.noexcept:
                self._safe_sendintr()
                self.captured_error = e
            else:
                raise

    def _safe_assert(self, cmd: str):
        try:
            assert_bash_exec(self.bash, cmd, want_output=None)
        except Exception as e:
            if self.noexcept:
                self._safe_sendintr()
                self.captured_error = e
            else:
                raise

    def _copy_variable(self, src_var: str, dst_var: str):
        self._safe_exec(
            "if [[ ${%s+set} ]]; then %s=${%s}; else unset -v %s; fi"
            % (src_var, dst_var, src_var, dst_var),
        )

    def _unset_variable(self, varname: str):
        self._safe_exec("unset -v %s" % varname)

    def _save_cwd(self):
        if not self.cwd_changed:
            self.cwd_changed = True
            self._copy_variable("PWD", "%s_OLDPWD" % self.prefix)

    def _check_set(self, name: str):
        if self.saved_set[name] != bash_env_saved.saved_state.ChangesDetected:
            return
        self._safe_assert(
            '[[ $(shopt -po %s) == "${%s_NEWSHOPT_%s}" ]]'
            % (name, self.prefix, name),
        )

    def _unprotect_set(self, name: str):
        if name not in self.saved_set:
            self.saved_set[name] = bash_env_saved.saved_state.ChangesDetected
            self._safe_exec(
                "%s_OLDSHOPT_%s=$(shopt -po %s || true)"
                % (self.prefix, name, name),
            )
        else:
            self._check_set(name)

    def _protect_set(self, name: str):
        self._safe_exec(
            "%s_NEWSHOPT_%s=$(shopt -po %s || true)"
            % (self.prefix, name, name),
        )

    def _check_shopt(self, name: str):
        if (
            self.saved_shopt[name]
            != bash_env_saved.saved_state.ChangesDetected
        ):
            return
        self._safe_assert(
            '[[ $(shopt -p %s) == "${%s_NEWSHOPT_%s}" ]]'
            % (name, self.prefix, name),
        )

    def _unprotect_shopt(self, name: str):
        if name not in self.saved_shopt:
            self.saved_shopt[name] = bash_env_saved.saved_state.ChangesDetected
            self._safe_exec(
                "%s_OLDSHOPT_%s=$(shopt -p %s || true)"
                % (self.prefix, name, name),
            )
        else:
            self._check_shopt(name)

    def _protect_shopt(self, name: str):
        self._safe_exec(
            "%s_NEWSHOPT_%s=$(shopt -p %s || true)"
            % (self.prefix, name, name),
        )

    def _check_variable(self, varname: str):
        if (
            self.saved_variables[varname]
            != bash_env_saved.saved_state.ChangesDetected
        ):
            return
        try:
            self._safe_assert(
                '[[ ${%s-%s} == "${%s_NEWVAR_%s-%s}" ]]'
                % (varname, MAGIC_MARK2, self.prefix, varname, MAGIC_MARK2),
            )
        except Exception:
            self._copy_variable(
                "%s_NEWVAR_%s" % (self.prefix, varname), varname
            )
            raise
        else:
            if self.noexcept and self.captured_error:
                self._copy_variable(
                    "%s_NEWVAR_%s" % (self.prefix, varname), varname
                )

    def _unprotect_variable(self, varname: str):
        if varname not in self.saved_variables:
            self.saved_variables[varname] = (
                bash_env_saved.saved_state.ChangesDetected
            )
            self._copy_variable(
                varname, "%s_OLDVAR_%s" % (self.prefix, varname)
            )
        else:
            self._check_variable(varname)

    def _protect_variable(self, varname: str):
        self._copy_variable(varname, "%s_NEWVAR_%s" % (self.prefix, varname))

    def _restore_env(self):
        self.noexcept = True

        if self.sendintr:
            self._safe_sendintr()

        # We first go back to the original directory before restoring
        # variables because "cd" affects "OLDPWD".
        if self.cwd_changed:
            self._unprotect_variable("OLDPWD")
            self._safe_exec('command cd -- "$%s_OLDPWD"' % self.prefix)
            self._protect_variable("OLDPWD")
            self._unset_variable("%s_OLDPWD" % self.prefix)
            self.cwd_changed = False

        for varname in self.saved_variables:
            self._check_variable(varname)
            self._copy_variable(
                "%s_OLDVAR_%s" % (self.prefix, varname), varname
            )
            self._unset_variable("%s_OLDVAR_%s" % (self.prefix, varname))
            self._unset_variable("%s_NEWVAR_%s" % (self.prefix, varname))
        self.saved_variables = {}

        for name in self.saved_shopt:
            self._check_shopt(name)
            self._safe_exec('eval "$%s_OLDSHOPT_%s"' % (self.prefix, name))
            self._unset_variable("%s_OLDSHOPT_%s" % (self.prefix, name))
            self._unset_variable("%s_NEWSHOPT_%s" % (self.prefix, name))
        self.saved_shopt = {}

        for name in self.saved_set:
            self._check_set(name)
            self._safe_exec('eval "$%s_OLDSHOPT_%s"' % (self.prefix, name))
            self._unset_variable("%s_OLDSHOPT_%s" % (self.prefix, name))
            self._unset_variable("%s_NEWSHOPT_%s" % (self.prefix, name))
        self.saved_set = {}

        self.noexcept = False
        if self.captured_error:
            raise self.captured_error

    def chdir(self, path: str):
        self._save_cwd()
        self.cwd_changed = True
        self._unprotect_variable("OLDPWD")
        self._safe_exec("command cd -- %s" % shlex.quote(path))
        self._protect_variable("OLDPWD")

    def set(self, name: str, value: bool):
        self._unprotect_set(name)
        if value:
            self._safe_exec("set -u %s" % name)
        else:
            self._safe_exec("set +o %s" % name)
        self._protect_set(name)

    def save_set(self, name: str):
        self._unprotect_set(name)
        self.saved_set[name] = bash_env_saved.saved_state.ChangesIgnored

    def shopt(self, name: str, value: bool):
        self._unprotect_shopt(name)
        if value:
            self._safe_exec("shopt -s %s" % name)
        else:
            self._safe_exec("shopt -u %s" % name)
        self._protect_shopt(name)

    def save_shopt(self, name: str):
        self._unprotect_shopt(name)
        self.saved_shopt[name] = bash_env_saved.saved_state.ChangesIgnored

    def write_variable(self, varname: str, new_value: str, quote: bool = True):
        if quote:
            new_value = shlex.quote(new_value)
        self._unprotect_variable(varname)
        self._safe_exec("%s=%s" % (varname, new_value))
        self._protect_variable(varname)

    def save_variable(self, varname: str):
        self._unprotect_variable(varname)
        self.saved_variables[varname] = (
            bash_env_saved.saved_state.ChangesIgnored
        )

    # TODO: We may restore the "export" attribute as well though it is
    #   not currently tested in "diff_env"
    def write_env(self, envname: str, new_value: str, quote: bool = True):
        if quote:
            new_value = shlex.quote(new_value)
        self._unprotect_variable(envname)
        self._safe_exec("export %s=%s" % (envname, new_value))
        self._protect_variable(envname)


def get_env(bash: pexpect.spawn) -> List[str]:
    return [
        x
        for x in assert_bash_exec(
            bash,
            "_comp__test_get_env",
            want_output=True,
        )
        .strip()
        .splitlines()
        # Sometimes there are empty lines in the output due to unknown
        # reasons, e.g. in GitHub Actions' macos-latest OS. Filter them out.
        if x
    ]


def diff_env(before: List[str], after: List[str], ignore: str):
    diff = [
        x
        for x in difflib.unified_diff(before, after, n=0, lineterm="")
        # Remove unified diff markers:
        if not re.search(r"^(---|\+\+\+|@@ )", x)
        # Ignore variables expected to change:
        and not re.search(
            r"^[-+](_|PPID|BASH_REMATCH|(BASH_)?LINENO)=",
            x,
            re.ASCII,
        )
        # Ignore likely completion functions added by us:
        and not re.search(r"^\+declare -f _.+", x)
        # ...and additional specified things:
        and not re.search(ignore or "^$", x)
    ]
    # For some reason, COMP_WORDBREAKS gets added to the list after
    # saving. Remove its changes, and note that it may take two lines.
    for i in range(0, len(diff)):
        if re.match("^[-+]COMP_WORDBREAKS=", diff[i]):
            if i < len(diff) and not re.match(r"^\+[\w]+=", diff[i + 1]):
                del diff[i + 1]
            del diff[i]
            break
    assert not diff, "Environment should not be modified"


class CompletionResult(Iterable[str]):
    """
    Class to hold completion results.
    """

    def __init__(self, output: Optional[str] = None):
        """
        :param output: All completion output as-is.
        """
        self.output = output or ""

    def endswith(self, suffix: str) -> bool:
        return self.output.endswith(suffix)

    def startswith(self, prefix: str) -> bool:
        return self.output.startswith(prefix)

    def _items(self) -> List[str]:
        return [x.strip() for x in self.output.strip().splitlines()]

    def __eq__(self, expected: object) -> bool:
        """
        Returns True if completion contains expected items, and no others.

        Defining __eq__ this way is quite ugly, but facilitates concise
        testing code.
        """
        if isinstance(expected, str):
            expiter = [expected]  # type: Iterable
        elif not isinstance(expected, Iterable):
            return False
        else:
            expiter = expected
        return self._items() == expiter

    def __contains__(self, item: str) -> bool:
        return item in self._items()

    def __iter__(self) -> Iterator[str]:
        return iter(self._items())

    def __len__(self) -> int:
        return len(self._items())

    def __repr__(self) -> str:
        return "<CompletionResult %s>" % self._items()


def assert_complete(
    bash: pexpect.spawn, cmd: str, **kwargs
) -> CompletionResult:
    skipif = kwargs.get("skipif")
    if skipif:
        try:
            assert_bash_exec(bash, skipif, want_output=None)
        except AssertionError:
            pass
        else:
            pytest.skip(skipif)
    xfail = kwargs.get("xfail")
    if xfail:
        try:
            assert_bash_exec(bash, xfail, want_output=None)
        except AssertionError:
            pass
        else:
            pytest.xfail(xfail)

    with bash_env_saved(bash, sendintr=True) as bash_env:
        cwd = kwargs.get("cwd")
        if cwd:
            bash_env.chdir(str(cwd))

        for k, v in kwargs.get("env", {}).items():
            bash_env.write_env(k, v, quote=False)

        for k, v in kwargs.get("shopt", {}).items():
            bash_env.shopt(k, v)

        input_cmd = cmd
        rendered_cmd = kwargs.get("rendered_cmd", cmd)
        re_MAGIC_MARK = re.escape(MAGIC_MARK)

        trail = kwargs.get("trail")
        if trail:
            # \002 = ^B = cursor left
            input_cmd += trail + "\002" * len(trail)
            rendered_cmd += trail + "\b" * len(trail)

            # After reading the results, something weird happens. For most test
            # setups, as expected (pun intended!), MAGIC_MARK follows as
            # is. But for some others (e.g. CentOS 6, Ubuntu 14 test
            # containers), we get MAGIC_MARK one character a time, followed
            # each time by trail and the corresponding number of \b's. Don't
            # know why, but accept it until/if someone finds out.  Or just be
            # fine with it indefinitely, the visible and practical end result
            # on a terminal is the same anyway.
            maybe_trail = "(%s%s)?" % (re.escape(trail), "\b" * len(trail))
            re_MAGIC_MARK = "".join(
                re.escape(x) + maybe_trail for x in MAGIC_MARK
            )

        bash.send(input_cmd + "\t")
        # Sleep a bit if requested, to avoid `.*` matching too early
        time.sleep(kwargs.get("sleep_after_tab", 0))
        bash.expect_exact(rendered_cmd)
        bash.send(MAGIC_MARK)
        got = bash.expect(
            [
                # 0: multiple lines, result in .before
                r"\r\n" + re.escape(PS1 + rendered_cmd) + ".*" + re_MAGIC_MARK,
                # 1: no completion
                r"^" + re_MAGIC_MARK,
                # 2: on same line, result in .match
                r"^([^\r]+)%s$" % re_MAGIC_MARK,
                # 3: error messages
                r"^([^\r].*)%s$" % re_MAGIC_MARK,
                pexpect.EOF,
                pexpect.TIMEOUT,
            ]
        )
        if got == 0:
            output = re.sub(re_MAGIC_MARK + "$", "", bash.before)
            return CompletionResult(output)
        elif got == 2:
            output = bash.match.group(1)
            return CompletionResult(output)
        elif got == 3:
            output = bash.match.group(1)
            raise AssertionError("Unexpected output: [%s]" % output)
        else:
            # TODO: warn about EOF/TIMEOUT?
            return CompletionResult()


@pytest.fixture
def completion(request, bash: pexpect.spawn) -> CompletionResult:
    marker = request.node.get_closest_marker("complete")
    if not marker:
        return CompletionResult()
    for pre_cmd in marker.kwargs.get("pre_cmds", []):
        assert_bash_exec(bash, pre_cmd, want_output=None)
    cmd = getattr(request.cls, "cmd", None)
    if marker.kwargs.get("require_longopt"):
        # longopt completions require both command presence and that it
        # responds something useful to --help
        if "require_cmd" not in marker.kwargs:
            marker.kwargs["require_cmd"] = True
        if "xfail" not in marker.kwargs:
            marker.kwargs["xfail"] = (
                # --help is required to exit with zero in order to not get a
                # positive for cases where it errors out with a message like
                # "foo: unrecognized option '--help'"
                "! %s --help &>/dev/null || "
                "! %s --help 2>&1 | command grep -qF -- --help"
            ) % ((cmd,) * 2)
    if marker.kwargs.get("require_cmd") and not is_bash_type(bash, cmd):
        pytest.skip("Command not found")

    return assert_complete(bash, marker.args[0], **marker.kwargs)


def in_container() -> bool:
    try:
        container = subprocess.check_output(
            "virt-what || systemd-detect-virt --container",
            stderr=subprocess.DEVNULL,
            shell=True,
        ).strip()
    except subprocess.CalledProcessError:
        container = b""
    if container and container != b"none":
        return True
    if os.path.exists("/.dockerenv"):
        return True
    try:
        with open("/proc/1/environ", "rb") as f:
            # LXC, others?
            if any(
                x.startswith(b"container=") for x in f.readline().split(b"\0")
            ):
                return True
    except OSError:
        pass
    return False


def prepare_fixture_dir(
    request, files: Iterable[str], dirs: Iterable[str]
) -> Tuple[Path, List[str], List[str]]:
    """
    Fixture to prepare a test dir with dummy contents on the fly.

    Tests that contain filenames differing only by case should use this to
    prepare a dir on the fly rather than including their fixtures in git and
    the tarball. This is to work better with case insensitive file systems.
    """
    tempdir = Path(tempfile.mkdtemp(prefix="bash-completion-fixture-dir"))
    request.addfinalizer(lambda: shutil.rmtree(str(tempdir)))

    old_cwd = os.getcwd()
    try:
        os.chdir(tempdir)
        new_files, new_dirs = create_dummy_filedirs(files, dirs)
    finally:
        os.chdir(old_cwd)

    return tempdir, new_files, new_dirs


def create_dummy_filedirs(
    files: Iterable[str], dirs: Iterable[str]
) -> Tuple[List[str], List[str]]:
    """
    Create dummy files and directories on the fly in the current directory.

    Tests that contain filenames differing only by case should use this to
    prepare a dir on the fly rather than including their fixtures in git and
    the tarball. This is to work better with case insensitive file systems.
    """
    new_files = []
    new_dirs = []

    for dir_ in dirs:
        path = Path(dir_)
        if not path.exists():
            path.mkdir()
            new_dirs.append(dir_)
    for file_ in files:
        path = Path(file_)
        if not path.exists():
            path.touch()
            new_files.append(file_)

    return sorted(new_files), sorted(new_dirs)


class TestUnitBase:
    def _test_unit(
        self, func, bash, comp_words, comp_cword, comp_line, comp_point, arg=""
    ):
        assert_bash_exec(
            bash,
            "COMP_WORDS=%s COMP_CWORD=%d COMP_LINE=%s COMP_POINT=%d"
            % (comp_words, comp_cword, shlex.quote(comp_line), comp_point),
        )
        output = assert_bash_exec(bash, func % arg, want_output=True)
        return output.strip()
