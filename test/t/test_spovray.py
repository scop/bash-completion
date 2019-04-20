import pytest


class TestSpovray:
    @pytest.mark.complete("spovray ")
    def test_1(self, completion):
        assert completion
