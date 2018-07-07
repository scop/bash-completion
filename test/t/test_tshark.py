import pytest


class TestTshark(object):

    @pytest.mark.complete("tshark -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("tshark -G ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("tshark -O foo,htt")
    def test_3(self, completion):
        assert completion.list
