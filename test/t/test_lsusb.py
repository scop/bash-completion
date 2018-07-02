import pytest


class Test(object):

    @pytest.mark.complete("lsusb -")
    def test_dash(self, completion):
        assert completion.list
