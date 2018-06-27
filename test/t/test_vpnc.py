import pytest


class Test(object):

    @pytest.mark.complete("vpnc -")
    def test_dash(self, completion):
        assert completion.list
