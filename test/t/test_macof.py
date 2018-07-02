import pytest


class Test(object):

    @pytest.mark.complete("macof -")
    def test_dash(self, completion):
        assert completion.list
