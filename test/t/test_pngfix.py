import pytest


class Test(object):

    @pytest.mark.complete("pngfix ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("pngfix -")
    def test_dash(self, completion):
        assert completion.list
