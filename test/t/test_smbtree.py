import pytest


class TestSmbtree(object):

    @pytest.mark.complete("smbtree -")
    def test_1(self, completion):
        assert completion.list
