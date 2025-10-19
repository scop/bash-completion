import pytest


class TestBase32:
    @pytest.mark.complete("base32 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("base32 -", require_longopt=True)
    def test_options(self, completion):
        assert completion
