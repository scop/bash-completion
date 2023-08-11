import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitGetFirstArg:
    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            '_comp__test_unit() { local -a "words=$1"; local cword=$2 ret=; shift 2; _comp_get_first_arg "$@" && printf "%s\\n" "$ret"; return 0; }',
        )

    def test_1(self, bash, functions):
        assert_bash_exec(bash, "_comp__test_unit '()' 0")

    def test_2(self, bash, functions):
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a b)" 2', want_output=None
        ).strip()
        assert output == "b"

    def test_3(self, bash, functions):
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a bc)" 2', want_output=None
        ).strip()
        assert output == "bc"

    def test_4(self, bash, functions):
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a b c)" 2', want_output=None
        ).strip()
        assert output == "b"

    def test_5(self, bash, functions):
        """Neither of the current word and the command name should be picked
        as the first argument"""
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a b c)" 1', want_output=None
        ).strip()
        assert output == ""

    def test_6(self, bash, functions):
        """Options starting with - should not be picked as the first
        argument"""
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a -b -c d e)" 4', want_output=None
        ).strip()
        assert output == "d"

    def test_7_single_hyphen(self, bash, functions):
        """- should be counted as an argument representing stdout/stdin"""
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a -b - c -d e)" 5', want_output=None
        ).strip()
        assert output == "-"

    def test_8_double_hyphen_1(self, bash, functions):
        """any word after -- should be picked"""
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a -b -- -c -d e)" 5', want_output=None
        ).strip()
        assert output == "-c"

    def test_8_double_hyphen_2(self, bash, functions):
        """any word after -- should be picked only without any preceding argument"""
        output = assert_bash_exec(
            bash, '_comp__test_unit "(a b -- -c -d e)" 5', want_output=None
        ).strip()
        assert output == "b"
