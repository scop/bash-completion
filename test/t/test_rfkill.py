import pytest


class TestRfkill:
    @pytest.mark.complete("rfkill ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rfkill -")
    def test_2(self, completion):
        assert completion
