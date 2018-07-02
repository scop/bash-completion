import pytest


class Test(object):

    @pytest.mark.complete("nslookup -")
    def test_dash(self, completion):
        assert completion.list
