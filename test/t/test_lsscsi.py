import pytest


class Test(object):

    @pytest.mark.complete("lsscsi ")
    def test_(self, completion):
        assert not completion.list

    @pytest.mark.complete("lsscsi -")
    def test_dash(self, completion):
        assert completion.list
