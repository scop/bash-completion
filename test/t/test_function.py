import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(ignore_env=r"^\+declare -f fn$")
class TestFunction:
    @pytest.mark.complete("function _parse_")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("function non_existent_function ")
    def test_2(self, completion):
        assert completion == "()"

    def test_3(self, bash):
        assert_bash_exec(bash, "fn() { echo; }")
        completion = assert_complete(bash, "function fn ")
        assert completion == "() { ^J    echo^J}"
