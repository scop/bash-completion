import pytest


class TestFreecivGtk2(object):

    @pytest.mark.complete("freeciv-gtk2 -")
    def test_1(self, completion):
        assert completion.list
