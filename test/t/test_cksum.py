import pytest


class TestCksum:
    @pytest.mark.complete("cksum ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cksum -", require_longopt=True)
    def test_options(self, completion):
        assert completion
