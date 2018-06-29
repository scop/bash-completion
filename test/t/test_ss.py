import pytest


class Test(object):

    @pytest.mark.complete("ss -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("ss -A ")
    def test_A(self, completion):
        assert completion.list

    @pytest.mark.complete("ss -A foo,")
    def test_A_comma(self, completion):
        assert completion.list
