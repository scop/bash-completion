import pytest


class Test(object):

    @pytest.mark.complete("display ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("display -")
    def test_dash(self, completion):
        assert completion.list
