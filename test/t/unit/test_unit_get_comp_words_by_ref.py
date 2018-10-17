import pytest

from conftest import assert_bash_exec, TestUnitBase


@pytest.mark.bashcomp(
    cmd=None, ignore_env=r"^(\+(cur|prev)|[+-]COMP_(WORDS|CWORD|LINE|POINT))=")
class TestUnitGetCompWordsByRef(TestUnitBase):

    def _test(self, bash, *args, **kwargs):
        assert_bash_exec(bash, "unset cur prev")
        output = self._test_unit(
            "_get_comp_words_by_ref %s cur prev; echo $cur,$prev",
            bash, *args, **kwargs)
        return output.strip()

    def test_1(self, bash):
        assert_bash_exec(bash, "_get_comp_words_by_ref cur >/dev/null")

    def test_2(self, bash):
        """a b|"""
        output = self._test(bash, "(a b)", 1, "a b", 3)
        assert output == "b,a"

    def test_3(self, bash):
        """a |"""
        output = self._test(bash, "(a)", 1, "a ", 2)
        assert output == ",a"

    def test_4(self, bash):
        """|a"""
        output = self._test(bash, "(a)", 0, "a", 0)
        assert output == ","

    def test_5(self, bash):
        """|a """
        output = self._test(bash, "(a)", 0, "a ", 0)
        assert output == ","

    def test_6(self, bash):
        """ | a """
        output = self._test(bash, "(a)", 0, "  a ", 1)
        assert output.strip() == ","

    def test_7(self, bash):
        """a b |"""
        output = self._test(bash, "(a b '')", 2, "a b ", 4)
        assert output == ",b"

    def test_8(self, bash):
        """a b | with WORDBREAKS -= :"""
        output = self._test(bash, "(a b '')", 2, "a b ", 4, arg="-n :")
        assert output == ",b"

    def test_9(self, bash):
        """a b|c"""
        output = self._test(bash, "(a bc)", 1, "a bc", 3)
        assert output == "b,a"

    def test_10(self, bash):
        """a | b"""
        output = self._test(bash, "(a b)", 1, "a  b", 2)
        assert output == ",a"

    def test_11(self, bash):
        r"""a b\ c|"""
        output = self._test(bash, r"(a 'b\ c')", 1, r"a b\ c", 6)
        assert output == r"b\ c,a"

    def test_12(self, bash):
        r"""a\ b a\ b|"""
        output = self._test(bash, r"('a\ b' 'a\ b')", 1, r"a\ b a\ b", 9)
        assert output == r"a\ b,a\ b"

    def test_13(self, bash):
        r"""a b\| c"""
        output = self._test(bash, r"(a 'b\ c')", 1, r"a b\ c", 4)
        assert output == r"b\,a"

    def test_14(self, bash):
        r"""a "b\|"""
        output = self._test(bash, "(a '\"b')", 1, 'a "b\\', 5)
        assert output == r'"b\,a'

    def test_15(self, bash):
        """a 'b c|"""
        output = self._test(bash, '(a "\'b c")', 1, "a 'b c", 6)
        assert output == "'b c,a"

    def test_16(self, bash):
        """a "b c|"""
        output = self._test(bash, r'(a "\"b c")', 1, 'a "b c', 6)
        assert output == '"b c,a'

    def test_17(self, bash):
        """a b:c| with WORDBREAKS += :"""
        assert_bash_exec(bash, "add_comp_wordbreak_char :")
        output = self._test(bash, "(a b : c)", 3, "a b:c", 5)
        assert output == "c,:"

    def test_18(self, bash):
        """a b:c| with WORDBREAKS -= :"""
        output = self._test(bash, "(a b : c)", 3, "a b:c", 5, arg="-n :")
        assert output == "b:c,a"

    def test_19(self, bash):
        """a b c:| with WORDBREAKS -= :"""
        output = self._test(bash, "(a b c :)", 3, "a b c:", 6, arg="-n :")
        assert output == "c:,b"

    def test_20(self, bash):
        r"""a b:c | with WORDBREAKS -= :"""
        output = self._test(bash, "(a b : c '')", 4, "a b:c ", 6, arg="-n :")
        assert output == ",b:c"

    def test_21(self, bash):
        """a :| with WORDBREAKS -= :"""
        output = self._test(bash, "(a :)", 1, "a :", 3, arg="-n :")
        assert output == ":,a"

    def test_22(self, bash):
        """a b::| with WORDBREAKS -= :"""
        output = self._test(bash, "(a b ::)", 2, "a b::", 5, arg="-n :")
        assert output == "b::,a"

    def test_23(self, bash):
        """a -n|

        This test makes sure `_get_cword' doesn't use `echo' to return its
        value, because -n might be interpreted by `echo' and thus woud not
        be returned.
        """
        output = self._test(bash, "(a -n)", 1, "a -n", 4)
        assert output == "-n,a"

    def test_24(self, bash):
        """a b>c|"""
        output = self._test(bash, r"(a b \> c)", 3, "a b>c", 5)
        assert output.startswith("c,")

    def test_25(self, bash):
        """a b=c|"""
        output = self._test(bash, "(a b = c)", 3, "a b=c", 5)
        assert output.startswith("c,")

    def test_26(self, bash):
        """a *|"""
        output = self._test(bash, r"(a \*)", 1, "a *", 4)
        assert output == "*,a"

    def test_27(self, bash):
        """a $(b c|"""
        output = self._test(bash, "(a '$(b c')", 1, "a $(b c", 7)
        assert output == "$(b c,a"

    def test_28(self, bash):
        r"""a $(b c\ d|"""
        output = self._test(bash, r"(a '$(b c\ d')", 1, r"a $(b c\ d", 10)
        assert output == r"$(b c\ d,a"

    def test_29(self, bash):
        """a 'b&c|"""
        output = self._test(bash, "(a \"'b&c\")", 1, "a 'b&c", 6)
        assert output == "'b&c,a"
