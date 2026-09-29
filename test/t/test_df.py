import pytest


class TestDf:
    @pytest.mark.complete("df ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("df -", require_longopt=True)
    def test_options(self, completion):
        assert completion
