import pytest


class TestUdevadm:

    @pytest.mark.complete("udevadm ")
    def test_1(self, completion):
        assert completion
