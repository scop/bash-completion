import pytest


class Test(object):

    @pytest.mark.complete("tracepath ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("tracepath -")
    def test_dash(self, completion):
        assert completion.list
