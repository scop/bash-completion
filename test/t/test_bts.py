import pytest


class TestBts:
    @pytest.mark.complete("bts ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("bts -")
    def test_2(self, completion):
        assert completion
