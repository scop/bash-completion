import pytest


class Test(object):

    @pytest.mark.complete("unace -")
    def test_dash(self, completion):
        assert completion.list
