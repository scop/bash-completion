import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitGetFirstArg:
    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            '_comp__test_unit() { local -a "words=$1"; local cword=$2 REPLY=; shift 2; _comp_get_first_arg "$@" && printf "%s\\n" "$REPLY"; return 0; }',
        )

    def _test(self, bash, words, cword, args=""):
        return assert_bash_exec(
            bash,
            '_comp__test_unit "%s" %d %s' % (words, cword, args),
            want_output=None,
        ).strip()

    def test_1(self, bash, functions):
        assert_bash_exec(bash, "_comp__test_unit '()' 0")

    def test_2(self, bash, functions):
        output = self._test(bash, "(a b)", 2)
        assert output == "b"

    def test_3(self, bash, functions):
        output = self._test(bash, "(a bc)", 2)
        assert output == "bc"

    def test_4(self, bash, functions):
        output = self._test(bash, "(a b c)", 2)
        assert output == "b"

    def test_5(self, bash, functions):
        """Neither of the current word and the command name should be picked
        as the first argument"""
        output = self._test(bash, "(a b c)", 1)
        assert output == ""

    def test_6(self, bash, functions):
        """Options starting with - should not be picked as the first
        argument"""
        output = self._test(bash, "(a -b -c d e)", 4)
        assert output == "d"

    def test_7_single_hyphen(self, bash, functions):
        """- should be counted as an argument representing stdout/stdin"""
        output = self._test(bash, "(a -b - c -d e)", 5)
        assert output == "-"

    def test_8_double_hyphen_1(self, bash, functions):
        """any word after -- should be picked"""
        output = self._test(bash, "(a -b -- -c -d e)", 5)
        assert output == "-c"

    def test_8_double_hyphen_2(self, bash, functions):
        """any word after -- should be picked only without any preceding argument"""
        output = self._test(bash, "(a b -- -c -d e)", 5)
        assert output == "b"

    def test_9_skip_optarg_1(self, bash, functions):
        output = self._test(bash, "(a -b -c d e f)", 5, '-a "@(-c|--foo)"')
        assert output == "e"

    def test_9_skip_optarg_2(self, bash, functions):
        output = self._test(bash, "(a -b --foo d e f)", 5, '-a "@(-c|--foo)"')
        assert output == "e"

    def test_9_skip_optarg_3(self, bash):
        output = self._test(bash, "(a -b - c d e)", 5, '-a "-b"')
        assert output == "c"

    def test_9_skip_optarg_4(self, bash):
        output = self._test(bash, "(a -b -c d e f)", 5, '-a "-[bc]"')
        assert output == "d"

    def test_9_skip_optarg_5(self, bash):
        output = self._test(bash, "(a +o b c d)", 4, '-a "+o"')
        assert output == "c"

    def test_9_skip_optarg_6(self, bash):
        output = self._test(bash, "(a -o -o -o -o b c)", 6, '-a "-o"')
        assert output == "b"

    def test_9_skip_optarg_7(self, bash):
        output = self._test(bash, "(a -o -- -b -c d e)", 6, '-a "-o"')
        assert output == "d"
