import difflib
import os
import re
import shlex
import subprocess
import time
from typing import Callable, Iterable, Iterator, List, Optional, Tuple

import pexpect
import pytest

PS1 = "/@"
MAGIC_MARK = "__MaGiC-maRKz!__"


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
        '_known_hosts_real ""; '
        r'printf "%s\n" "${COMPREPLY[@]}"; unset COMPREPLY',
        want_output=True,
    )
    return sorted(set(output.split()))


@pytest.fixture(scope="class")
def user_home(bash: pexpect.spawn) -> Tuple[str, str]:
    user = assert_bash_exec(
        bash, 'id -un 2>/dev/null || echo "$USER"', want_output=True
    ).strip()
    home = assert_bash_exec(bash, 'echo "$HOME"', want_output=True).strip()
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

    logfile = None
    if os.environ.get("BASHCOMP_TEST_LOGFILE"):
        logfile = open(os.environ["BASHCOMP_TEST_LOGFILE"], "w")
    testdir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)
    )
    env = os.environ.copy()
    env.update(
        dict(
            SRCDIR=testdir,  # TODO needed at least by bashrc
            SRCDIRABS=testdir,  # TODO needed?
            PS1=PS1,
            INPUTRC="%s/config/inputrc" % testdir,
            TERM="dumb",
            LC_COLLATE="C",  # to match Python's default locale unaware sort
        )
    )

    fixturesdir = os.path.join(testdir, "fixtures")
    os.chdir(fixturesdir)

    # Start bash
    bash = pexpect.spawn(
        "%s --norc" % os.environ.get("BASHCOMP_TEST_BASH", "bash"),
        maxread=os.environ.get("BASHCOMP_TEST_PEXPECT_MAXREAD", 20000),
        logfile=logfile,
        cwd=fixturesdir,
        env=env,
        encoding="utf-8",  # TODO? or native or...?
        # FIXME: Tests shouldn't depend on dimensions, but it's difficult to
        # expect robustly enough for Bash to wrap lines anywhere (e.g. inside
        # MAGIC_MARK).  Increase window width to reduce wrapping.
        dimensions=(24, 160),
        # TODO? codec_errors="replace",
    )
    bash.expect_exact(PS1)

    # Load bashrc and bash_completion
    assert_bash_exec(bash, "source '%s/config/bashrc'" % testdir)
    assert_bash_exec(bash, "source '%s/../bash_completion'" % testdir)

    # Use command name from marker if set, or grab from test filename
    cmd = None  # type: Optional[str]
    cmd_found = False
    marker = request.node.get_closest_marker("bashcomp")
    if marker:
        cmd = marker.kwargs.get("cmd")
        cmd_found = "cmd" in marker.kwargs
        # Run pre-test commands, early so they're usable in skipif
        for pre_cmd in marker.kwargs.get("pre_cmds", []):
            assert_bash_exec(bash, pre_cmd)
        # Process skip and xfail conditions
        skipif = marker.kwargs.get("skipif")
        if skipif:
            try:
                assert_bash_exec(bash, skipif, want_output=None)
            except AssertionError:
                pass
            else:
                bash.close()
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
            assert_bash_exec(bash, post_cmd)

    # Clean up
    bash.close()
    if logfile:
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
        # Allow __load_completion to fail so we can test completions
        # that are directly loaded in bash_completion without a separate file.
        assert_bash_exec(bash, "__load_completion %s || :" % cmd)
        assert_bash_exec(bash, "complete -p %s &>/dev/null" % cmd)
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
                % (cmd, status, output)
            )
        else:
            assert not want_output, (
                'Expected output from "%s": exit status=%s, output="%s"'
                % (cmd, status, output)
            )

    return output


def get_env(bash: pexpect.spawn) -> List[str]:
    return (
        assert_bash_exec(
            bash,
            "{ (set -o posix ; set); declare -F; shopt -p; set -o; }",
            want_output=True,
        )
        .strip()
        .splitlines()
    )


def diff_env(before: List[str], after: List[str], ignore: str):
    diff = [
        x
        for x in difflib.unified_diff(before, after, n=0, lineterm="")
        # Remove unified diff markers:
        if not re.search(r"^(---|\+\+\+|@@ )", x)
        # Ignore variables expected to change:
        and not re.search("^[-+](_|PPID|BASH_REMATCH|OLDPWD)=", x)
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
    cwd = kwargs.get("cwd")
    if cwd:
        assert_bash_exec(bash, "cd '%s'" % cwd)
    env_prefix = "_BASHCOMP_TEST_"
    env = kwargs.get("env", {})
    if env:
        # Back up environment and apply new one
        assert_bash_exec(
            bash,
            " ".join('%s%s="${%s-}"' % (env_prefix, k, k) for k in env.keys()),
        )
        assert_bash_exec(
            bash,
            "export %s" % " ".join("%s=%s" % (k, v) for k, v in env.items()),
        )
    try:
        bash.send(cmd + "\t")
        # Sleep a bit if requested, to avoid `.*` matching too early
        time.sleep(kwargs.get("sleep_after_tab", 0))
        bash.expect_exact(cmd)
        bash.send(MAGIC_MARK)
        got = bash.expect(
            [
                # 0: multiple lines, result in .before
                r"\r\n" + re.escape(PS1 + cmd) + ".*" + re.escape(MAGIC_MARK),
                # 1: no completion
                r"^" + re.escape(MAGIC_MARK),
                # 2: on same line, result in .match
                r"^([^\r]+)%s$" % re.escape(MAGIC_MARK),
                pexpect.EOF,
                pexpect.TIMEOUT,
            ]
        )
        if got == 0:
            output = bash.before
            if output.endswith(MAGIC_MARK):
                output = bash.before[: -len(MAGIC_MARK)]
            result = CompletionResult(output)
        elif got == 2:
            output = bash.match.group(1)
            result = CompletionResult(output)
        else:
            # TODO: warn about EOF/TIMEOUT?
            result = CompletionResult()
    finally:
        bash.sendintr()
        bash.expect_exact(PS1)
        if env:
            # Restore environment, and clean up backup
            # TODO: Test with declare -p if a var was set, backup only if yes, and
            #       similarly restore only backed up vars. Should remove some need
            #       for ignore_env.
            assert_bash_exec(
                bash,
                "export %s"
                % " ".join(
                    '%s="$%s%s"' % (k, env_prefix, k) for k in env.keys()
                ),
            )
            assert_bash_exec(
                bash,
                "unset -v %s"
                % " ".join("%s%s" % (env_prefix, k) for k in env.keys()),
            )
        if cwd:
            assert_bash_exec(bash, "cd - >/dev/null")
    return result


@pytest.fixture
def completion(request, bash: pexpect.spawn) -> CompletionResult:
    marker = request.node.get_closest_marker("complete")
    if not marker:
        return CompletionResult()
    for pre_cmd in marker.kwargs.get("pre_cmds", []):
        assert_bash_exec(bash, pre_cmd)
    cmd = getattr(request.cls, "cmd", None)
    if marker.kwargs.get("require_longopt"):
        # longopt completions require both command presence and that it
        # responds something useful to --help
        if "require_cmd" not in marker.kwargs:
            marker.kwargs["require_cmd"] = True
        if "xfail" not in marker.kwargs:
            marker.kwargs["xfail"] = (
                "! %s --help &>/dev/null || "
                "! %s --help 2>&1 | command grep -qF -- --help"
            ) % ((cmd,) * 2)
    if marker.kwargs.get("require_cmd") and not is_bash_type(bash, cmd):
        pytest.skip("Command not found")

    if "trail" in marker.kwargs:
        return assert_complete_at_point(
            bash, cmd=marker.args[0], trail=marker.kwargs["trail"]
        )

    return assert_complete(bash, marker.args[0], **marker.kwargs)


def assert_complete_at_point(
    bash: pexpect.spawn, cmd: str, trail: str
) -> CompletionResult:
    # TODO: merge to assert_complete
    fullcmd = "%s%s%s" % (
        cmd,
        trail,
        "\002" * len(trail),
    )  # \002 = ^B = cursor left
    bash.send(fullcmd + "\t")
    bash.send(MAGIC_MARK)
    bash.expect_exact(fullcmd.replace("\002", "\b"))

    got = bash.expect_exact(
        [
            # 0: multiple lines, result in .before
            PS1 + fullcmd.replace("\002", "\b"),
            # 1: no completion
            MAGIC_MARK,
            pexpect.EOF,
            pexpect.TIMEOUT,
        ]
    )
    if got == 0:
        output = bash.before
        result = CompletionResult(output)

        # At this point, something weird happens. For most test setups, as
        # expected (pun intended!), MAGIC_MARK follows as is. But for some
        # others (e.g. CentOS 6, Ubuntu 14 test containers), we get MAGIC_MARK
        # one character a time, followed each time by trail and the corresponding
        # number of \b's. Don't know why, but accept it until/if someone finds out.
        # Or just be fine with it indefinitely, the visible and practical end
        # result on a terminal is the same anyway.
        repeat = "(%s%s)?" % (re.escape(trail), "\b" * len(trail))
        fullexpected = "".join(
            "%s%s" % (re.escape(x), repeat) for x in MAGIC_MARK
        )
        bash.expect(fullexpected)
    else:
        # TODO: warn about EOF/TIMEOUT?
        result = CompletionResult()

    return result


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
