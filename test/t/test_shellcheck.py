import pytest


class TestShellcheck:
    @pytest.mark.complete("shellcheck ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("shellcheck -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("shellcheck --format=", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("shellcheck -s ", require_cmd=True)
    def test_4(self, completion):
        assert "bash" in completion

    @pytest.mark.complete(
        "shellcheck -S ",
        require_cmd=True,
        skipif="! shellcheck --help | command grep -qF -- --severity",
    )
    def test_severity_arg(self, completion):
        assert completion
