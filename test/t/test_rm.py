import pytest


class TestRm(object):

    @pytest.mark.complete("rm ")
    def test_1(self, completion):
        assert completion.list
