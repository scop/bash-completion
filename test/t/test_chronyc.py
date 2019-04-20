import pytest


class TestChronyc:
    @pytest.mark.complete("chronyc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chronyc -")
    def test_2(self, completion):
        assert completion
