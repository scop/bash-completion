import pytest


class TestDhclient(object):

    @pytest.mark.complete("dhclient -")
    def test_1(self, completion):
        assert completion.list
