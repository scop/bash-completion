import pytest


class Test(object):

    @pytest.mark.complete("pkg-config ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("pkg-config -")
    def test_dash(self, completion):
        assert completion.list
