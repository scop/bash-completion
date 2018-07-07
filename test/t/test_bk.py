import pytest


class TestBk(object):

    @pytest.mark.complete("bk ")
    def test_1(self, completion):
        assert completion.list
