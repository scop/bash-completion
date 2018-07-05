import pytest


class Test(object):

    @pytest.mark.complete("ncftp ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ncftp -")
    def test_dash(self, completion):
        assert completion.list
