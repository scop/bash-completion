import pytest


class Test(object):

    @pytest.mark.complete("xmodmap ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xmodmap -")
    def test_dash(self, completion):
        assert completion.list
