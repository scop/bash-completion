import pytest


class TestVmstat:
    @pytest.mark.complete("vmstat -", require_cmd=True)
    def test_1(self, completion):
        assert completion
