import pytest


class TestLspci:
    @pytest.mark.complete("lspci -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lspci -A ")
    def test_2(self, completion):
        assert completion
