import pytest


class Test(object):

    @pytest.mark.complete("mii-diag ")
    def test_(self, completion):
        assert completion.list
