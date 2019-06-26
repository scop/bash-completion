import pytest


class TestNgrep:
    @pytest.mark.complete("ngrep -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ngrep -d ")
    def test_2(self, completion):
        assert completion
