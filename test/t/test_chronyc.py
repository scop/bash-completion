import pytest


class Test(object):

    @pytest.mark.complete("chronyc ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("chronyc -")
    def test_dash(self, completion):
        assert completion.list
