import pytest


class TestG++(object):

    @pytest.mark.complete("g++ ")
    def test_1(self, completion):
        assert completion.list
