import pytest


class TestUdevadm:
    @pytest.mark.complete("udevadm ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("udevadm -")
    def test_2(self, completion):
        assert completion
