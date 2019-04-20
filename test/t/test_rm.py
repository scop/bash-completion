import pytest


class TestRm:
    @pytest.mark.complete("rm ")
    def test_1(self, completion):
        assert completion
