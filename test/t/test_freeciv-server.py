import pytest


class Test(object):

    @pytest.mark.complete("freeciv-server -")
    def test_dash(self, completion):
        assert completion.list
