import pytest


class TestBase64:
    @pytest.mark.complete("base64 ")
    def test_1(self, completion):
        assert completion
