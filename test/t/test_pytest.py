import pytest


class Test(object):

    @pytest.mark.complete("pytest ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("pytest -")
    def test_dash(self, completion):
        assert completion.list
