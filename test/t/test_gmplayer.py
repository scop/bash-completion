import pytest


class Test(object):

    @pytest.mark.complete("gmplayer ")
    def test_(self, completion):
        assert completion.list
