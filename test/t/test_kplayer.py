import pytest


class TestKplayer(object):

    @pytest.mark.complete("kplayer ")
    def test_1(self, completion):
        assert completion.list
