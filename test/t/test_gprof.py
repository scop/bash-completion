import pytest


class TestGprof:
    @pytest.mark.complete("gprof --", require_cmd=True)
    def test_1(self, completion):
        assert completion
