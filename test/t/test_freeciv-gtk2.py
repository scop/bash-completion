import pytest


class Test(object):

    @pytest.mark.complete("freeciv-gtk2 -")
    def test_dash(self, completion):
        assert completion.list
