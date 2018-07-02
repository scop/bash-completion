import pytest


class Test(object):

    @pytest.mark.complete("gnome-mplayer ")
    def test_(self, completion):
        assert completion.list
