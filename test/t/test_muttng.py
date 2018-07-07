import pytest


class TestMuttng(object):

    @pytest.mark.complete("muttng -")
    def test_1(self, completion):
        assert completion.list
