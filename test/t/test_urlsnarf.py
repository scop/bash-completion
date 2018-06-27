import pytest


class Test(object):

    @pytest.mark.complete("urlsnarf -")
    def test_dash(self, completion):
        assert completion.list
