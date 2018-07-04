import pytest


class Test(object):

    @pytest.mark.complete("arping ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("arping -")
    def test_dash(self, completion):
        assert completion.list
