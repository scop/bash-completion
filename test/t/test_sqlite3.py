import pytest


class Test(object):

    @pytest.mark.complete("sqlite3 ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("sqlite3 -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("sqlite3 -scratch foo ")
    def test_scratch(self, completion):
        assert not completion.list
