import pytest


class TestLzip:
    @pytest.mark.complete("lzip ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lzip -")
    def test_2(self, completion):
        assert completion
