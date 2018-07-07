import pytest


class TestLinks(object):

    @pytest.mark.complete("links ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("links -")
    def test_2(self, completion):
        assert completion.list
