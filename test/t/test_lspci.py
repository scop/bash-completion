import pytest


class Test(object):

    @pytest.mark.complete("lspci -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("lspci -A ")
    def test_a(self, completion):
        assert completion.list
