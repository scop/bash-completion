import pytest


class TestWebmitm:
    @pytest.mark.complete("webmitm -")
    def test_1(self, completion):
        assert completion
