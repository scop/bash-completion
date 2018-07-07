import pytest


class TestIptables(object):

    @pytest.mark.complete("iptables -")
    def test_1(self, completion):
        assert completion.list
