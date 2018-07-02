import pytest


class Test(object):

    @pytest.mark.complete("pvmove --")
    def test_dash(self, completion):
        assert completion.list
