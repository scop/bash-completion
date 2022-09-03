from shlex import quote

import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


def join(words):
    """Return a shell-escaped string from *words*."""
    return " ".join(quote(word) for word in words)


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-]COMPREPLY=",
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


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^[+-]ret=")
class TestUnitCommandOffsetReduceCur:
    def check(self, bash, cur, expected):
        assert (
            assert_bash_exec(
                bash,
                '_comp_command_offset__reduce_cur %s; echo "$ret"'
                % quote(cur),
                want_output=True,
            ).strip("\r\n")
            == expected
        )

    @pytest.mark.parametrize(
        "cur,expected",
        [
            ("==", ""),
            ("=:", ""),
            ("--foo'=", "="),
            ("=", ""),
            ("'=", "="),
            ("'='", "'='"),
            ('a"b', "b"),
            ('a"b"', 'a"b"'),
            ('a"b"c', 'a"b"c'),
            ('a"b"c"', ""),
            ("a", "a"),
            ("ab", "ab"),
            ("abc", "abc"),
            ("abcd", "abcd"),
            ('a"a$(echo', "a$(echo"),
            ('a"a$(echo "', 'a"a$(echo "'),
            ('a"a$(echo "world"x', "x"),
            ('a"a$(echo "world"x)', "x)"),
            ("a${va", "a${va"),
            ("$'a", "a"),
            ("$'a\\n", "a\\n"),
            ("$'a\\n\\'", "$'a\\n\\'"),
            ("$'a\\n\\' '", ""),
            ("$'a\\n\\' \\'x", "$'a\\n\\' \\'x"),
            ("$'a\\n\\' \\'xyz'x", "x"),
            ("a'bb\\'aaa", "a'bb\\'aaa"),
            ("a'bb\\'aaa'c", "c"),
            ('a"bb', "bb"),
            ('a"bb\\"a', 'bb\\"a'),
            ('a"bb\\"a"c', 'a"bb\\"a"c'),
            ("a`", "a`"),
            ("a`echo", "a`echo"),
            ("a`echo w", "w"),
            ('a"echo ', "echo "),
            ('a"echo w', "echo w"),
            ("$'a\\' x", "$'a\\' x"),
            ("a`bbb ccc`", "ccc`"),
            ("a`aa'a", "a"),
            ('a`aa"aa', "aa"),
            ("a`aa$'a\\'a a", "a`aa$'a\\'a a"),
            ("a`b$'c\\'d e", "a`b$'c\\'d e"),
            ("$'c\\'d e`f g", "$'c\\'d e`f g"),
            ("$'c\\'d e'f`g h", "f`g h"),
            ("$'a b'c`d e", "e"),
            ("a`b'c'd e", "e"),
            ("a`b'c'd e f", "f"),
            ("a`$(echo world", "world"),
            ("a`$'a\\' b", "a`$'a\\' b"),
            ("a`$'b c\\'d e$'f g\\'", "g\\'"),
            ("a`$'b c\\'d e$'f g\\'h i", "i"),
            ("a`$'b c\\'d e$'f g\\'h i`j", "i`j"),
            ("a`$'b c\\'d e'f g'", "g'"),
            ("a`a;", ""),
            ("a`x=", ""),
            ("a`x=y", "y"),
            ("a`b|", ""),
            ("a`b:c", "c"),
            ("a`b&", ""),
        ],
    )
    def test_1(self, bash, cur, expected):
        self.check(bash, cur, expected)

    def test_COMP_WORDBREAKS_atmark(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("COMP_WORDBREAKS", "@$IFS", quote=False)
            self.check(bash, "a`b@", "@")
            self.check(bash, "a`b@c", "@c")
            self.check(bash, "a`b@@c", "@c")
            self.check(bash, "a`b@@c@", "@")

    def test_COMP_WORDBREAKS_z(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote("z"), quote=False
            )
            self.check(bash, "a`b;c", "a`b;c")
            self.check(bash, "a`bzc", "c")
            self.check(bash, "a`bzcdze", "e")
            self.check(bash, "a`bzcdzze", "e")
            self.check(bash, "a`bzcdzzze", "e")
            self.check(bash, "a`b\\zc", "a`b\\zc")

    def test_COMP_WORDBREAKS_dollar(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote("$"), quote=False
            )
            self.check(bash, "a`b$'hxy'", "a`b$'hxy'")
            self.check(bash, "a`b$", "$")
            self.check(bash, "a`b$x", "$x")
            self.check(bash, "a`b${", "${")
            self.check(bash, "a`b${x}", "${x}")
            self.check(bash, "a`b${x}y", "${x}y")
            self.check(bash, "a`b$=", "$=")
            self.check(bash, "a`b$.", "$.")
            self.check(bash, "a`b$'a'", "a`b$'a'")
            self.check(bash, 'a`b$"a"', '$"a"')
            self.check(bash, "a'b", "b")
            self.check(bash, "a`b$'' a$'xyz", "xyz")

    def test_COMP_WORDBREAKS_backslash(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote("\\"), quote=False
            )
            self.check(bash, r"a`b\cd", "cd")
            self.check(bash, r"a`b\cde\fg", "fg")
            self.check(bash, r"a`b\c\\a", r"\a")
            self.check(bash, r"a`b\c\\\a", "a")
            self.check(bash, r"a`b\c\\\\a", r"\a")
            self.check(bash, r"a`b\c\a\a", "a")
            self.check(bash, "a`b\\", "")
            self.check(bash, "a`b\\\\", "\\")
            self.check(bash, "a`b\\\\\\", "")

    def test_COMP_WORDBREAKS_dollar_backslash(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote("$\\"), quote=False
            )
            self.check(bash, "a`b$\\", "")
            self.check(bash, "a`b\\$", "$")

    def test_COMP_WORDBREAKS_dollar_atmark_z(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote("$@z"), quote=False
            )
            self.check(bash, "a$z", "")
            self.check(bash, "a$$z", "")
            self.check(bash, "a$$", "$")
            self.check(bash, "a$@", "@")
            self.check(bash, "a$$@", "@")

    def test_COMP_WORDBREAKS_dollar_backquote(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote("`"), quote=False
            )
            self.check(bash, "a`b`", "")

    @pytest.mark.parametrize("symbol", list("!#%*+,-./?[]^_}~"))
    def test_COMP_WORDBREAKS_symbol(self, bash, symbol):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "COMP_WORDBREAKS", "%s$IFS" % quote(symbol), quote=False
            )
            self.check(bash, "a`b%s" % symbol, "")
            self.check(bash, "a`b%sc" % symbol, "c")
