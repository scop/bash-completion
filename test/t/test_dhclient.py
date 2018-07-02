import pytest


class Test(object):

    @pytest.mark.complete("dhclient -")
    def test_dash(self, completion):
        assert completion.list
