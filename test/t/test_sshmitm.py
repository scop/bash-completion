import pytest


class TestSshmitm:
    @pytest.mark.complete("sshmitm -")
    def test_1(self, completion):
        assert completion
