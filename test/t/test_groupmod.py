import pytest


class Test(object):

    @pytest.mark.complete("groupmod ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("groupmod -")
    def test_dash(self, completion):
        assert completion.list
