import pytest


class Test(object):

    @pytest.mark.complete("route ")
    def test_(self, completion):
        assert completion.list
