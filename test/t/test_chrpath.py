import pytest


class Test(object):

    @pytest.mark.complete("chrpath ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("chrpath -")
    def test_dash(self, completion):
        assert completion.list
