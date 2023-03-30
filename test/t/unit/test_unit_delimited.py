import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitDelimited:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            "_comp_cmd_test_delim() {"
            "  local cur prev words cword comp_args;"
            "  _comp_get_words cur;"
            "  _comp_delimited , -W 'alpha beta bravo';"
            "};"
            "complete -F _comp_cmd_test_delim test_delim",
        )

    @pytest.mark.complete("test_delim --opt=a")
    def test_1(self, functions, completion):
        assert completion == ["lpha"]

    @pytest.mark.complete("test_delim --opt=b")
    def test_2(self, functions, completion):
        assert completion == ["beta", "bravo"]

    @pytest.mark.complete("test_delim --opt=alpha,b")
    def test_3(self, functions, completion):
        assert completion == ["alpha,beta", "alpha,bravo"]

    @pytest.mark.complete("test_delim --opt=alpha,be")
    def test_4(self, functions, completion):
        assert completion == ["ta"]

    @pytest.mark.complete("test_delim --opt=beta,a")
    def test_5(self, functions, completion):
        assert completion == ["lpha"]

    @pytest.mark.complete("test_delim --opt=c")
    def test_6(self, functions, completion):
        assert not completion
