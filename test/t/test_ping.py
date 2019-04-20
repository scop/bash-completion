import pytest


class TestPing:
    @pytest.mark.complete("ping ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ping -")
    def test_2(self, completion):
        assert completion
