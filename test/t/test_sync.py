import pytest


class TestSync:
    @pytest.mark.complete("sync ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sync -", require_longopt=True)
    def test_options(self, completion):
        assert completion
