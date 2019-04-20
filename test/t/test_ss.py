import pytest


class TestSs:
    @pytest.mark.complete("ss -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ss -A ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("ss -A foo,")
    def test_3(self, completion):
        assert completion
