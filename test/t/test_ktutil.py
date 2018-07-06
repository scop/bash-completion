import pytest


class Test(object):

    @pytest.mark.complete("ktutil ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ktutil -")
    def test_dash(self, completion):
        assert completion.list
