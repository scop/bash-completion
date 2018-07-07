import pytest


class TestVpnc(object):

    @pytest.mark.complete("vpnc -")
    def test_1(self, completion):
        assert completion.list
