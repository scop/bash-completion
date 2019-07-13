import pytest


class TestTee:
    @pytest.mark.complete("tee ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tee -", require_longopt=True)
    def test_options(self, completion):
        assert completion
