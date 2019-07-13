import pytest


class TestBase64:
    @pytest.mark.complete("base64 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("base64 -", require_longopt=True)
    def test_options(self, completion):
        assert completion
