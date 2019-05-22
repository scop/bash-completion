import pytest


class TestGnokii:
    @pytest.mark.complete("gnokii ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gnokii -")
    def test_2(self, completion):
        assert completion
