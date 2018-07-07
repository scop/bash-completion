import pytest


class TestTac(object):

    @pytest.mark.complete("tac --")
    def test_1(self, completion):
        assert completion.list
