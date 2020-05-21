import pexpect
import pytest

from conftest import PS1, TestUnitBase, assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None, ignore_env=r"^[+-](COMP_(WORDS|CWORD|LINE|POINT)|_scp_path_esc)="
)
class TestUnitGetCword(TestUnitBase):
    def _test(self, *args, **kwargs):
        return self._test_unit("_get_cword %s; echo", *args, **kwargs)

    def test_1(self, bash):
        assert_bash_exec(
            bash,
            "COMP_WORDS=() COMP_CWORD= COMP_LINE= COMP_POINT= "
            "_get_cword >/dev/null",
        )

    def test_2(self, bash):
        """a b| should return b"""
        output = self._test(bash, "(a b)", 1, "a b", 3)
        assert output == "b"

    def test_3(self, bash):
        """a | should return nothing"""
        output = self._test(bash, "(a)", 1, "a ", 2)
        assert not output

    def test_4(self, bash):
        """a b | should return nothing"""
        output = self._test(bash, "(a b '')", 2, "a b ", 4)
        assert not output

    def test_5(self, bash):
        """a b | with WORDBREAKS -= : should return nothing"""
        output = self._test(bash, "(a b '')", 2, "a b ", 4, arg=":")
        assert not output

    def test_6(self, bash):
        """a b|c should return b"""
        output = self._test(bash, "(a bc)", 1, "a bc", 3)
        assert output == "b"

    def test_7(self, bash):
        r"""a b\ c| should return b\ c"""
        output = self._test(bash, r"(a 'b\ c')", 1, r"a b\ c", 6)
        assert output == r"b\ c"

    def test_8(self, bash):
        r"""a b\| c should return b\ """
        output = self._test(bash, r"(a 'b\ c')", 1, r"a b\ c", 4)
        assert output == "b\\"

    def test_9(self, bash):
        r"""a "b\| should return "b\ """
        output = self._test(bash, "(a '\"b\\')", 1, r"a \"b\\", 5)
        assert output == '"b\\'

    def test_10(self, bash):
        r"""a 'b c| should return 'b c"""
        output = self._test(bash, '(a "\'b c")', 1, "a 'b c", 6)
        assert output == "'b c"

    def test_11(self, bash):
        r"""a "b c| should return "b c"""
        output = self._test(bash, "(a '\"b c')", 1, 'a "b c', 6)
        assert output == '"b c'

    def test_12(self, bash):
        """a b:c| with WORDBREAKS += : should return c"""
        assert_bash_exec(bash, "add_comp_wordbreak_char :")
        output = self._test(bash, "(a b : c)", 3, "a b:c", 5)
        assert output == "c"

    def test_13(self, bash):
        """a b:c| with WORDBREAKS -= : should return b:c"""
        assert_bash_exec(bash, "add_comp_wordbreak_char :")
        output = self._test(bash, "(a b : c)", 3, "a b:c", 5, arg=":")
        assert output == "b:c"

    def test_14(self, bash):
        """a b c:| with WORDBREAKS -= : should return c:"""
        assert_bash_exec(bash, "add_comp_wordbreak_char :")
        output = self._test(bash, "(a b c :)", 3, "a b c:", 6, arg=":")
        assert output == "c:"

    def test_15(self, bash):
        """a :| with WORDBREAKS -= : should return :"""
        assert_bash_exec(bash, "add_comp_wordbreak_char :")
        output = self._test(bash, "(a :)", 1, "a :", 3, arg=":")
        assert output == ":"

    def test_16(self, bash):
        """a b::| with WORDBREAKS -= : should return b::"""
        assert_bash_exec(bash, "add_comp_wordbreak_char :")
        output = self._test(bash, "(a b::)", 1, "a b::", 5, arg=":")
        assert output == "b::"

    def test_17(self, bash):
        """
        a -n| should return -n

        This test makes sure `_get_cword' doesn't use `echo' to return its
        value, because -n might be interpreted by `echo' and thus woud not
        be returned.
        """
        output = self._test(bash, "(a -n)", 1, "a -n", 4)
        assert output == "-n"

    def test_18(self, bash):
        """a b>c| should return c"""
        output = self._test(bash, r"(a b \> c)", 3, "a b>c", 5)
        assert output == "c"

    def test_19(self, bash):
        """a b=c| should return c"""
        output = self._test(bash, "(a b = c)", 3, "a b=c", 5)
        assert output == "c"

    def test_20(self, bash):
        """a *| should return *"""
        output = self._test(bash, r"(a \*)", 1, "a *", 4)
        assert output == "*"

    def test_21(self, bash):
        """a $(b c| should return $(b c"""
        output = self._test(bash, r"(a '$(b c')", 1, "a $(b c", 7)
        assert output == "$(b c"

    def test_22(self, bash):
        r"""a $(b c\ d| should return $(b c\ d"""
        output = self._test(bash, r"(a '$(b c\ d')", 1, r"a $(b c\ d", 10)
        assert output == r"$(b c\ d"

    def test_23(self, bash):
        """a 'b&c| should return 'b&c"""
        output = self._test(bash, '(a "\'b&c")', 1, "a 'b&c", 6)
        assert output == "'b&c"

    @pytest.mark.xfail(reason="TODO: non-ASCII issues with test suite?")
    def test_24(self, bash):
        """Index shouldn't drop below 0"""
        bash.send("scp ääää§ se\t\r\n")
        got = bash.expect_exact(
            [
                "index: substring expression < 0",
                PS1,
                pexpect.EOF,
                pexpect.TIMEOUT,
            ]
        )
        assert got == 1
