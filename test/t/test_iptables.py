import pytest


class Test(object):

    @pytest.mark.complete("iptables -")
    def test_dash(self, completion):
        assert completion.list
