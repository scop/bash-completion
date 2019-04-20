import pytest


class TestNgrep:
    @pytest.mark.complete("ngrep -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ngrep -d ")
    def test_2(self, completion):
        assert completion
