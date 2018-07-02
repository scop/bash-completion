import pytest


class Test(object):

    @pytest.mark.complete("2to3 ")
    def test_(self, completion):
        assert completion.list
