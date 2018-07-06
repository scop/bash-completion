import pytest


class Test(object):

    @pytest.mark.complete("dselect ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("dselect -")
    def test_dash(self, completion):
        assert completion.list
