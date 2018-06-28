import pytest


class Test(object):

    @pytest.mark.complete("tightvncviewer ")
    def test_(self, completion):
        assert completion.list
