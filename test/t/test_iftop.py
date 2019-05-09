import pytest


class TestIftop:
    @pytest.mark.complete("iftop ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("iftop -")
    def test_2(self, completion):
        assert completion
