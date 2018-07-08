import pytest


class TestFreecivServer(object):

    @pytest.mark.complete("freeciv-server -")
    def test_1(self, completion):
        assert completion.list
