import pytest


class Test(object):

    @pytest.mark.complete("g4 ")
    def test_(self, completion):
        assert completion.list
