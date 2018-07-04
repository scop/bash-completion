import pytest


class Test(object):

    @pytest.mark.complete("bind -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("bind k")
    def test_k(self, completion):
        assert completion.list
