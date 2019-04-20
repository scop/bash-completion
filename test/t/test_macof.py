import pytest


class TestMacof:
    @pytest.mark.complete("macof -")
    def test_1(self, completion):
        assert completion
