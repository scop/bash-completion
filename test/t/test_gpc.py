import pytest


class Test(object):

    @pytest.mark.complete("gpc ")
    def test_(self, completion):
        assert completion.list
