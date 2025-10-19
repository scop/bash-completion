import pytest


class TestStat:
    @pytest.mark.complete("stat ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("stat -", require_longopt=True)
    def test_options(self, completion):
        assert completion
