import pytest


class TestMiiDiag(object):

    @pytest.mark.complete("mii-diag ")
    def test_1(self, completion):
        assert completion.list
