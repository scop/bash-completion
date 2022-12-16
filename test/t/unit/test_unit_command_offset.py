from shlex import quote

import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


def join(words):
    """Return a shell-escaped string from *words*."""
    return " ".join(quote(word) for word in words)


@pytest.mark.bashcomp(
    cmd=None,
    cwd="_command_offset",
    ignore_env=r"^[+-](COMPREPLY|REPLY)=",
)
class TestUnitCommandOffset:
    wordlist = sorted(["foo", "bar"])

    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            "_cmd1() { _comp_command_offset 1; }; complete -F _cmd1 cmd1; "
            "complete -F _comp_command meta; "
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

        assert_bash_exec(
            bash, "complete -W %s 'cmd!'" % quote(join(self.wordlist))
        )
        assert_bash_exec(bash, 'complete -W \'"$word1" "$word2"\' cmd6')

        assert_bash_exec(bash, "complete -C ./completer cmd7")

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

    @pytest.mark.parametrize(
        "cmd,expected_completion",
        [
            ("cmd7 ", wordlist),
            ("cmd7 l", ["line\\^Jtwo", "long"]),
            ("cmd7 lo", ["ng"]),
            ("cmd7 line", ["\\^Jtwo"]),
            ("cmd7 cont1", ["cont10", "cont11\\"]),
        ],
    )
    def test_3(self, bash, functions, cmd, expected_completion):
        got = assert_complete(bash, f"cmd1 {cmd}")
        assert got == assert_complete(bash, cmd)
        assert got == expected_completion

    def test_cmd_quoted(self, bash, functions):
        assert assert_complete(bash, "meta 'cmd2' ") == self.wordlist

    def test_cmd_specialchar(self, bash, functions):
        assert assert_complete(bash, "meta 'cmd!' ") == self.wordlist

    def test_space(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("word1", "a b c")
            bash_env.write_variable("word2", "d e f")
            assert assert_complete(bash, "meta cmd6 ") == ["a b c", "d e f"]

    @pytest.fixture(scope="class")
    def find_original_word_functions(self, bash):
        assert_bash_exec(
            bash,
            "_comp_test_reassemble() {"
            "    local IFS=$' \\t\\n' REPLY;"
            '    COMP_LINE=$1; _comp_split COMP_WORDS "$2"; COMP_CWORD=$((${#COMP_WORDS[@]}-1));'
            "    _comp__reassemble_words = words cword;"
            "}",
        )
        assert_bash_exec(
            bash,
            "_comp_test_1() {"
            '    local COMP_WORDS COMP_LINE COMP_CWORD words cword REPLY; _comp_test_reassemble "$1" "$2";'
            '    _comp__find_original_word "$3";'
            '    echo "$REPLY";'
            "}",
        )

    def test_find_original_word_1(self, bash, find_original_word_functions):
        result = assert_bash_exec(
            bash,
            '_comp_test_1 "sudo su do su do abc" "sudo su do su do abc" 3',
            want_output=True,
        ).strip()
        assert result == "3"

    def test_find_original_word_2(self, bash, find_original_word_functions):
        result = assert_bash_exec(
            bash,
            '_comp_test_1 "sudo --prefix=su su do abc" "sudo --prefix = su su do abc" 2',
            want_output=True,
        ).strip()
        assert result == "4"
