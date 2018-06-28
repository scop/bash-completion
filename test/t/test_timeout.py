import pytest


class Test(object):

    @pytest.mark.complete("timeout ")
    def test_(self, completion):
        assert not completion.list

    @pytest.mark.complete("timeout -")
    def test_dash(self, completion):
        assert completion.list
