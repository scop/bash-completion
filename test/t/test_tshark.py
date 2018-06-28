import pytest


class Test(object):

    @pytest.mark.complete("tshark -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("tshark -G ")
    def test_G(self, completion):
        assert completion.list

    @pytest.mark.complete("tshark -O foo,htt")
    def test_O_comma(self, completion):
        assert completion.list
