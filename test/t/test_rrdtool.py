import pytest


class Test(object):

    @pytest.mark.complete("rrdtool ")
    def test_(self, completion):
        assert completion.list
