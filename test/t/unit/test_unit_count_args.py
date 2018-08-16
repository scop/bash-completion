import shlex

import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None,
                      ignore_env=r"^[+-](args|COMP_(WORDS|CWORD|LINE|POINT))=")
class TestUnitCountArgs:

    def _test(self, bash,
              comp_words, comp_cword, comp_line, comp_point, arg=""):
        assert_bash_exec(
            bash,
            "COMP_WORDS=%s COMP_CWORD=%d COMP_LINE=%s COMP_POINT=%d" %
            (comp_words, comp_cword, shlex.quote(comp_line), comp_point))
        output = assert_bash_exec(
            bash, "_count_args %s; echo $args" % arg, want_output=True)
        return output.strip()

    def test_1(self, bash):
        assert_bash_exec(bash, "_count_args >/dev/null")

    def test_2(self, bash):
        """a b| should set args to 1"""
        output = self._test(bash, "(a b)", 1, "a b", 3)
        assert output == "1"

    def test_3(self, bash):
        """a b|c should set args to 1"""
        output = self._test(bash, "(a bc)", 1, "a bc", 3)
        assert output == "1"

    def test_4(self, bash):
        """a b c| should set args to 2"""
        output = self._test(bash, "(a b c)", 2, "a b c", 4)
        assert output == "2"

    def test_5(self, bash):
        """a b| c should set args to 1"""
        output = self._test(bash, "(a b c)", 1, "a b c", 3)
        assert output == "1"

    def test_6(self, bash):
        """a b -c| d should set args to 2"""
        output = self._test(bash, "(a b -c d)", 2, "a b -c d", 6)
        assert output == "2"

    def test_7(self, bash):
        """a b -c| d e should set args to 2"""
        output = self._test(bash, "(a b -c d e)", 4, "a b -c d e", 6,
                            '"" "@(-c|--foo)"')
        assert output == "2"
