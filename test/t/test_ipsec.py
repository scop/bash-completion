import pytest


class Test(object):

    @pytest.mark.complete("ipsec ")
    def test_(self, completion):
        assert completion.list
