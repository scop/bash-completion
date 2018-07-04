import pytest


class Test(object):

    @pytest.mark.complete("gdb - ")
    def test_dash(self, completion):
        assert completion.list
