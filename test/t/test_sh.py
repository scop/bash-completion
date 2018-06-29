import pytest


class Test(object):

    @pytest.mark.complete("sh -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("sh +")
    def test_plus(self, completion):
        assert completion.list

    @pytest.mark.complete("sh -o ")
    def test_o(self, completion):
        assert completion.list

    @pytest.mark.complete("sh -c ")
    def test_c(self, completion):
        assert not completion.list
