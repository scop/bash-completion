import pytest


class TestBadblocks(object):

    @pytest.mark.complete("badblocks ")
    def test_1(self, completion):
        assert completion.list
