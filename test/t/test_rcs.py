import pytest


class TestRcs:
    @pytest.mark.complete("rcs ")
    def test_1(self, completion):
        assert completion
