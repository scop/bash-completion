import pytest


class TestDmesg:
    @pytest.mark.complete("dmesg -", require_cmd=True)
    def test_1(self, completion):
        assert completion
