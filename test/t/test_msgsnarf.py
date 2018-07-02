import pytest


class Test(object):

    @pytest.mark.complete("msgsnarf -")
    def test_dash(self, completion):
        assert completion.list
