import pytest


class TestUdevadm(object):

    @pytest.mark.complete("udevadm ")
    def test_1(self, completion):
        assert completion.list
