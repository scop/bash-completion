import pytest


class Test(object):

    @pytest.mark.complete("tac --")
    def test_dash(self, completion):
        assert completion.list
