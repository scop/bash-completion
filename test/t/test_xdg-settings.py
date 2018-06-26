import pytest


class Test(object):

    @pytest.mark.complete("xdg-settings ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-settings --")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-settings get ")
    def test_get(self, completion):
        assert completion.list
