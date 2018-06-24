import pytest


class Test(object):

    @pytest.mark.complete("xmlwf ")
    def test_(self, completion):
        assert completion.list
