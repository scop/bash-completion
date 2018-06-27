import pytest


class Test(object):

    @pytest.mark.complete("usermod ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("usermod -")
    def test_dash(self, completion):
        assert completion.list
