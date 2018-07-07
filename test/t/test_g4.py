import pytest


class TestG4(object):

    @pytest.mark.complete("g4 ")
    def test_1(self, completion):
        assert completion.list
