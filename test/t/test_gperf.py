import pytest


class TestGperf:
    @pytest.mark.complete("gperf --", require_cmd=True)
    def test_1(self, completion):
        assert completion
