import pytest


class TestKtutil:
    @pytest.mark.complete("ktutil ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ktutil -")
    def test_2(self, completion):
        assert completion
