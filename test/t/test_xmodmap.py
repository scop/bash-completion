import pytest


class Test(object):

    @pytest.mark.complete("xmodmap ")
    def test_(self, completion):
        assert completion.list
