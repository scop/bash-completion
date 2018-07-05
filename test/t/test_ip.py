import pytest


class Test(object):

    @pytest.mark.complete("ip ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ip a ")
    def test_a(self, completion):
        assert completion.list
