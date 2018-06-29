import pytest


class Test(object):

    @pytest.mark.complete("reptyr ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("reptyr -")
    def test_dash(self, completion):
        assert completion.list
