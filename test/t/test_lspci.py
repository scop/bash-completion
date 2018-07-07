import pytest


class TestLspci(object):

    @pytest.mark.complete("lspci -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("lspci -A ")
    def test_2(self, completion):
        assert completion.list
