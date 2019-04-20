import pytest


class TestLsusb:
    @pytest.mark.complete("lsusb -")
    def test_1(self, completion):
        assert completion
