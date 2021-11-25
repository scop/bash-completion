from shlex import quote

import pytest

from conftest import assert_bash_exec, assert_complete


def join(words):
    """Return a shell-escaped string from *words*."""
    return " ".join(quote(word) for word in words)


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](COMP(_(WORDS|CWORD|LINE|POINT)|REPLY)|cur|cword|words)=",
)
class TestUnitCommandOffset:
    wordlist = sorted(["foo", "bar"])

    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            "_cmd1() { _command_offset 1; }; complete -F _cmd1 cmd1; "
            "complete -F _command meta; "
            "_compfunc() { COMPREPLY=(%s); }" % join(self.wordlist),
        )
        completions = [
            'complete -F _compfunc "${COMP_WORDS[0]}"',
            'complete -W %s "${COMP_WORDS[0]}"' % quote(join(self.wordlist)),
            'COMPREPLY=(dummy); complete -r "${COMP_WORDS[0]}"',
            "COMPREPLY+=(${#COMPREPLY[@]})",
        ]

        for idx, comp in enumerate(completions, 2):
            assert_bash_exec(
                bash,
                "_cmd%(idx)s() { %(comp)s && return 124; }; "
                "complete -F _cmd%(idx)s cmd%(idx)s"
                % {"idx": idx, "comp": comp},
            )

    def test_1(self, bash, functions):
        assert_complete(bash, 'cmd1 "/tmp/aaa bbb" ')
        assert_bash_exec(bash, "! complete -p aaa", want_output=None)

    @pytest.mark.parametrize(
        "cmd,expected_completion",
        [
            ("cmd2", wordlist),
            ("cmd3", wordlist),
            ("cmd4", []),
            ("cmd5", ["0"]),
        ],
    )
    def test_2(self, bash, functions, cmd, expected_completion):
        """Test meta-completion for completion functions that signal that
        completion should be retried (i.e. change compspec and return 124).

        cmd2: The case when the completion spec is overwritten by the one that
        contains "-F func"

        cmd3: The case when the completion spec is overwritten by the one
        without "-F func".

        cmd4: The case when the completion spec is removed, in which we expect
        no completions.  This mimics the behavior of Bash's progcomp for the
        exit status 124.

        cmd5: The case when the completion spec is unchanged.  The retry should
        be attempted at most once to avoid infinite loops.  COMPREPLY should be
        cleared before the retry.
        """
        assert assert_complete(bash, "meta %s " % cmd) == expected_completion
