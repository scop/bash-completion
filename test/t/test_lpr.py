import pytest


class Test(object):

    @pytest.mark.complete("lpr ")
    def test_(self, completion):
        assert completion.list
