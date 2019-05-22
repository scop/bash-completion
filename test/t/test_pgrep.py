import pytest


class TestPgrep:

    # "p": Assume that our process name completion runs ps
    @pytest.mark.complete("pgrep p")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pgrep -")
    def test_2(self, completion):
        assert completion
