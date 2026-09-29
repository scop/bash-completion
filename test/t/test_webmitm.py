import pytest


class TestWebmitm:
    @pytest.mark.complete("webmitm -", require_cmd=True)
    def test_1(self, completion):
        assert completion
