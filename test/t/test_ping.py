import pytest


class Test(object):

    @pytest.mark.complete("ping ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ping -")
    def test_dash(self, completion):
        assert completion.list
