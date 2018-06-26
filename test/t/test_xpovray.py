import pytest


class Test(object):

    @pytest.mark.complete("xpovray ")
    def test_(self, completion):
        assert completion.list
