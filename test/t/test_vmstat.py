import pytest


class TestVmstat:
    @pytest.mark.complete("vmstat -")
    def test_1(self, completion):
        assert completion
