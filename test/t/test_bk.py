import pytest


class TestBk:
    @pytest.mark.complete("bk ")
    def test_1(self, completion):
        assert completion
