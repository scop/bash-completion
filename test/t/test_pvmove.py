import pytest


class TestPvmove(object):

    @pytest.mark.complete("pvmove --")
    def test_1(self, completion):
        assert completion.list
