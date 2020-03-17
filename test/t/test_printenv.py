import pytest


class TestPrintenv:
    @pytest.mark.complete("printenv ")
    def test_empty(self, completion):
        assert completion

    @pytest.mark.complete("printenv PAT")
    def test_path(self, completion):
        assert "PATH" in completion

    @pytest.mark.complete("printenv -", require_cmd=True)
    def test_options(self, completion):
        assert completion
