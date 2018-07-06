import pytest


class Test(object):

    @pytest.mark.complete("ipv6calc -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("ipv6calc --in ")
    def test_in(self, completion):
        assert completion.list
