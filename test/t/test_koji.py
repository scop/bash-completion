import pytest


class Test(object):

    @pytest.mark.complete("koji ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("koji -")
    def test_dash(self, completion):
        assert completion.list
