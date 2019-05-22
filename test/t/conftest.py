import difflib
import os
import re
import shlex
import subprocess
from typing import Iterable, List, Optional, Tuple, Union

import pexpect
import pytest


PS1 = "/@"
MAGIC_MARK = "__MaGiC-maRKz!__"


def find_unique_completion_pair(
    items: Iterable[str]
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
def part_full_user(bash: pexpect.spawn) -> Optional[Tuple[str, str]]:
    res = (
        assert_bash_exec(bash, "compgen -u", want_output=True).strip().split()
    )
    pair = find_unique_completion_pair(res)
    if not pair:
        pytest.skip("No suitable test user found")
    return pair


@pytest.fixture(scope="class")
def part_full_group(bash: pexpect.spawn) -> Optional[Tuple[str, str]]:
    res = (
        assert_bash_exec(bash, "compgen -g", want_output=True).strip().split()
    )
    pair = find_unique_completion_pair(res)
    if not pair:
        pytest.skip("No suitable test user found")
    return pair


@pytest.fixture(scope="class")
def bash(request) -> pexpect.spawn:

    logfile = None
    if os.environ.get("BASHCOMP_TEST_LOGFILE"):
        logfile = open(os.environ.get("BASHCOMP_TEST_LOGFILE"), "w")
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
    cmd = None
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
                assert_bash_exec(bash, skipif)
            except AssertionError:
                pass
            else:
                bash.close()
                pytest.skip(skipif)
                return
        xfail = marker.kwargs.get("xfail")
        if xfail:
            try:
                assert_bash_exec(bash, xfail)
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


def is_testable(bash: pexpect.spawn, cmd: str) -> bool:
    if not cmd:
        pytest.fail("Could not resolve name of command to test")
        return False
    if not is_bash_type(bash, cmd):
        pytest.skip("Command %s not found" % cmd)
        return False
    if not load_completion_for(bash, cmd):
        pytest.skip("No completion for command %s" % cmd)
        return False
    return True


def is_bash_type(bash: pexpect.spawn, cmd: str) -> bool:
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
    bash: pexpect.spawn, cmd: str, want_output: bool = False, want_newline=True
) -> str:

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


class CompletionResult:
    """
    Class to hold completion results.
    """

    def __init__(self, output: str, items: Optional[Iterable[str]] = None):
        """
        When items are specified, they are used as the base for comparisons
        provided by this class. When not, regular expressions are used instead.
        This is because it is not always possible to unambiguously split a
        completion output string into individual items, for example when the
        items contain whitespace.

        :param output: All completion output as-is.
        :param items: Completions as individual items. Should be specified
            only in cases where the completions are robustly known to be
            exactly the specified ones.
        """
        self.output = output
        self._items = None if items is None else sorted(items)

    def endswith(self, suffix: str) -> bool:
        return self.output.endswith(suffix)

    def __eq__(self, expected: Union[str, Iterable[str]]) -> bool:
        """
        Returns True if completion contains expected items, and no others.

        Defining __eq__ this way is quite ugly, but facilitates concise
        testing code.
        """
        expiter = [expected] if isinstance(expected, str) else sorted(expected)
        if self._items is not None:
            return self._items == expiter
        return bool(
            re.match(
                r"^\s*" + r"\s+".join(re.escape(x) for x in expiter) + r"\s*$",
                self.output,
            )
        )

    def __contains__(self, item: str) -> bool:
        if self._items is not None:
            return item in self._items
        return bool(
            re.search(r"(^|\s)%s(\s|$)" % re.escape(item), self.output)
        )

    def __iter__(self) -> Iterable[str]:
        """
        Note that iteration over items may not be accurate when items were not
        specified to the constructor, if individual items in the output contain
        whitespace. In those cases, it errs on the side of possibly returning
        more items than there actually are, and intends to never return fewer.
        """
        return iter(
            self._items
            if self._items is not None
            else re.split(r" {2,}|\r\n", self.output.strip())
        )

    def __len__(self) -> int:
        """
        Uses __iter__, see caveat in it. While possibly inaccurate, this is
        good enough for truthiness checks.
        """
        return len(list(iter(self)))

    def __repr__(self) -> str:
        return "<CompletionResult %s>" % list(self)


def assert_complete(
    bash: pexpect.spawn, cmd: str, **kwargs
) -> CompletionResult:
    skipif = kwargs.get("skipif")
    if skipif:
        try:
            assert_bash_exec(bash, skipif)
        except AssertionError:
            pass
        else:
            pytest.skip(skipif)
            return CompletionResult("", [])
    xfail = kwargs.get("xfail")
    if xfail:
        try:
            assert_bash_exec(bash, xfail)
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
            " ".join('%s%s="$%s"' % (env_prefix, k, k) for k in env.keys()),
        )
        assert_bash_exec(
            bash,
            "export %s" % " ".join("%s=%s" % (k, v) for k, v in env.items()),
        )
    bash.send(cmd + "\t")
    bash.expect_exact(cmd)
    bash.send(MAGIC_MARK)
    got = bash.expect(
        [
            # 0: multiple lines, result in .before
            r"\r\n" + re.escape(PS1 + cmd) + ".*" + MAGIC_MARK,
            # 1: no completion
            r"^" + MAGIC_MARK,
            # 2: on same line, result in .match
            r"^([^\r]+)%s$" % MAGIC_MARK,
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
        result = CompletionResult(output, [shlex.split(cmd + output)[-1]])
    else:
        # TODO: warn about EOF/TIMEOUT?
        result = CompletionResult("", [])
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
            % " ".join('%s="$%s%s"' % (k, env_prefix, k) for k in env.keys()),
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
        return CompletionResult("", [])
    for pre_cmd in marker.kwargs.get("pre_cmds", []):
        assert_bash_exec(bash, pre_cmd)
    return assert_complete(bash, marker.args[0], **marker.kwargs)


def in_container() -> bool:
    try:
        container = subprocess.check_output(
            "virt-what || systemd-detect-virt --container",
            stderr=subprocess.DEVNULL,
            shell=True,
        ).strip()
    except subprocess.CalledProcessError:
        container = None
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
