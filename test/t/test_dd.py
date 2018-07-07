import pytest


class Test(object):

    @pytest.mark.complete("dd --")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("dd bs")
    def test_bs(self, completion):
        assert completion.list == ["bs="]
