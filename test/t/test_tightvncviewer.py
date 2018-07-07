import pytest


class TestTightvncviewer(object):

    @pytest.mark.complete("tightvncviewer ")
    def test_1(self, completion):
        assert completion.list
