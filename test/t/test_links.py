import pytest


class Test(object):

    @pytest.mark.complete("links ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("links -")
    def test_dash(self, completion):
        assert completion.list
