import pytest


class TestGperf:
    @pytest.mark.complete("gperf --")
    def test_1(self, completion):
        assert completion
