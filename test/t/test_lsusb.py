import pytest


class TestLsusb(object):

    @pytest.mark.complete("lsusb -")
    def test_1(self, completion):
        assert completion.list
