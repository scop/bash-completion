import pytest


class Test(object):

    @pytest.mark.complete("ngrep -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("ngrep -d ")
    def test_d(self, completion):
        assert completion.list
