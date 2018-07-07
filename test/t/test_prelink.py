import pytest


class TestPrelink(object):

    @pytest.mark.complete("prelink ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("prelink -")
    def test_2(self, completion):
        assert completion.list
