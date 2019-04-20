import pytest


class TestPvmove:
    @pytest.mark.complete("pvmove --")
    def test_1(self, completion):
        assert completion
