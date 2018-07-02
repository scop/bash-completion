import pytest


class Test(object):

    @pytest.mark.complete("checksec -")
    def test_dash(self, completion):
        assert completion.list
