import pytest


class TestNewlist(object):

    @pytest.mark.complete("newlist -")
    def test_1(self, completion):
        assert completion.list
