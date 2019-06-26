import pytest


class TestSshmitm:
    @pytest.mark.complete("sshmitm -", require_cmd=True)
    def test_1(self, completion):
        assert completion
