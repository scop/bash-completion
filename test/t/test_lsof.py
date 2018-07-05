import pytest


class Test(object):

    @pytest.mark.complete("lsof ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("lsof -")
    def test_dash(self, completion):
        assert completion.list
