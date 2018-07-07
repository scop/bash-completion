import pytest


class TestXdgSettings(object):

    @pytest.mark.complete("xdg-settings ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-settings --")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-settings get ")
    def test_3(self, completion):
        assert completion.list
