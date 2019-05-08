import pytest


class TestE2freefrag:
    @pytest.mark.complete("e2freefrag ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("e2freefrag -")
    def test_2(self, completion):
        assert completion
