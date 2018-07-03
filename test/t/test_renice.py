import pytest


class Test(object):

    @pytest.mark.complete("renice 1")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("renice -g ")
    def test_g(self, completion):
        assert completion.list
