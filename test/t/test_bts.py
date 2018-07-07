import pytest


class TestBts(object):

    @pytest.mark.complete("bts ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("bts -")
    def test_2(self, completion):
        assert completion.list
