import pytest


class TestPrintenv:
    @pytest.mark.complete("printenv ")
    def test_empty(self, completion):
        assert completion

    @pytest.mark.complete("printenv PAT")
    def test_path(self, completion):
        assert completion == "H" or "PATH" in completion

    @pytest.mark.complete(
        "printenv -",
        require_cmd=True,
        xfail="! printenv --help 2>&1 | command grep -qF -- ' -'",
    )
    def test_options(self, completion):
        assert completion
