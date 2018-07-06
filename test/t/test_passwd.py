import pytest


class Test(object):

    @pytest.mark.complete("passwd ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("passwd -")
    def test_(self, completion):
        assert completion.list
