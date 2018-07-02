import pytest


class Test(object):

    @pytest.mark.complete("kplayer ")
    def test_(self, completion):
        assert completion.list
