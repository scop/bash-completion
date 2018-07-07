import pytest


class TestPgrep(object):

    # "p": Assume that our process name completion runs ps
    @pytest.mark.complete("pgrep p")
    def test_1(self, completion):
        assert completion.list
