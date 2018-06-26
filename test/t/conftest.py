import difflib
import os
import re
import shlex
from typing import List, NamedTuple

import pexpect
import pytest


PS1 = "/@"
MAGIC_MARK = "__MaGiC-maRKz!__"


@pytest.fixture(autouse=True, scope="class")
def bash(request) -> pexpect.spawn:

    testdir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
    env = dict(
        SRCDIR=testdir,  # TODO needed at least by bashrc
        SRCDIRABS=testdir,  # TODO needed?
        PS1=PS1,
        INPUTRC="%s/config/inputrc" % testdir,
        TERM="dumb",
        BASH_COMPLETION_COMPAT_DIR="%s/fixtures/shared/empty_dir" % testdir,
    )
    # TODO set stty_init "columns 150" --> dimensions? needed in first place?

    # Start bash
    bash = pexpect.spawn(
        "%s --norc" % os.environ.get("BASHCOMP_BASH", "bash"),
        maxread=os.environ.get("BASHCOMP_PEXPECT_MAXREAD", 20000),
        cwd=os.path.join(testdir, "fixtures"),
        env=env,
        encoding="utf-8",  # TODO? or native or...?
        # TODO? codec_errors="replace",
    )

    # Load bashrc and bash_completion
    assert_bash_exec(bash, "source '%s/config/bashrc'" % testdir)
    assert_bash_exec(bash, "source '%s/../bash_completion'" % testdir)

    # Use command name from marker if set, or grab from test filename
    cmd = None
    marker = request.node.get_marker("command")
    if marker:
        cmd = marker.args[0]
    else:
        match = re.search(r"^test_(.+)\.py$", os.path.basename(request.fspath))
        if match:
            cmd = match.group(1)

    if is_testable(bash, cmd):
        before_env = get_env(bash)
        yield bash
        diff_env(before_env, get_env(bash))

    # Clean up
    bash.close()


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
    loadcmd = "__load_completion %s; " \
              "complete -p %s &>/dev/null && echo -n 0 || echo -n 1" % \
              (cmd, cmd)
    bash.sendline(loadcmd)
    # TODO: why doesn't expect_exact(loadcmd + "\r\n") work here?
    bash.expect(".*?\r\n")
    result = bash.expect_exact(["0", "1"]) == 0
    bash.expect_exact(PS1)
    return result


def assert_bash_exec(
        bash: pexpect.spawn, cmd: str, want_output: bool = False) -> str:

    # Send command
    bash.sendline(cmd)
    bash.expect_exact(cmd)

    # Find prompt, output is before it
    bash.expect_exact("\r\n" + PS1)
    output = bash.before

    # Retrieve exit status
    echo = "echo $?"
    bash.sendline(echo)
    got = bash.expect([
        r"^%s\r\n(\d+)\r\n%s" % (re.escape(echo), re.escape(PS1)),
        PS1,
        pexpect.EOF,
        pexpect.TIMEOUT,
    ])
    status = bash.match.group(1) if got == 0 else "unknown"

    assert status == "0", \
        'Error running "%s": exit status=%s, output="%s"' % \
        (cmd, status, output)
    if output:
        assert want_output, \
            'Unexpected output from "%s": exit status=%s, output="%s"' % \
            (cmd, status, output)
    else:
        assert not want_output, \
            'Expected output from "%s": exit status=%s, output="%s"' % \
            (cmd, status, output)

    return output


def get_env(bash: pexpect.spawn) -> List[str]:
    return assert_bash_exec(
        bash,
        "{ (set -o posix ; set); declare -F; shopt -p; set -o; }",
        want_output=True
    ).strip().splitlines()


def diff_env(before: List[str], after: List[str]):
    diff = [
        x for x in
        difflib.unified_diff(before, after, n=0, lineterm="")
        # Remove unified diff markers:
        if not re.search(r"^(---|\+\+\+|@@ )", x)
        # Ignore variables expected to change:
        and not re.search("^[-+](_|PPID|BASH_REMATCH)=", x)
        # Ignore likely completion functions added by us:
        and not re.search(r"^\+declare -f _.+", x)

    ]
    # For some reason, COMP_WORDBREAKS gets added to the list after
    # saving. Remove its changes, and note that it may take two lines.
    for i in range(0, len(diff)):
        if re.match("^[-+]COMP_WORDBREAKS=", diff[i]):
            if i < len(diff) and not re.match(r"^\+[\w]+=", diff[i+1]):
                del diff[i+1]
            del diff[i]
            break
    assert not diff, "Environment should not be modified"


class CompletionResult(NamedTuple):
    line: str
    list: List[str]


@pytest.fixture(autouse=True)
def completion(request, bash: pexpect.spawn) -> CompletionResult:
    cmd = request.node.get_marker("complete").args[0]
    bash.send(cmd + "\t")
    bash.expect_exact(cmd)
    bash.send(MAGIC_MARK)
    got = bash.expect([
        r"\r\n" + re.escape(PS1 + cmd),  # 0: multiple lines, result in .before
        r"^" + MAGIC_MARK,               # 1: no completion
        r"^[^\r]+",                      # 2: on same line, result in .after
        pexpect.EOF,
        pexpect.TIMEOUT,
    ])
    if got == 0:
        line = bash.before
        if line.endswith(MAGIC_MARK):
            line = bash.before[:-len(MAGIC_MARK)]
        result = CompletionResult(
            line,
            [x for x in re.split(r" {2,}|\r\n", line) if x],
        )
    elif got == 2:
        line = bash.after
        if line.endswith(MAGIC_MARK):
            line = bash.after[:-len(MAGIC_MARK)]
        result = CompletionResult(
            line,
            shlex.split(cmd + line)[-1],
        )
    else:
        # TODO: warn about EOF/TIMEOUT?
        result = CompletionResult("", [])
    bash.sendintr()
    bash.expect_exact(PS1)
    return result
