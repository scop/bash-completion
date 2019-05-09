import pytest


class TestMonodevelop:
    @pytest.mark.complete("monodevelop ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("monodevelop -")
    def test_2(self, completion):
        assert completion
