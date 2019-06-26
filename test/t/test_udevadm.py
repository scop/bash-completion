import pytest


class TestUdevadm:
    @pytest.mark.complete("udevadm ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("udevadm -", require_cmd=True)
    def test_2(self, completion):
        assert completion
