import pytest


class TestDmesg:
    @pytest.mark.complete("dmesg -")
    def test_1(self, completion):
        assert completion
