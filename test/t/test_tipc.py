import pytest


class Test(object):

    @pytest.mark.complete("tipc ")
    def test_(self, completion):
        assert completion.list
