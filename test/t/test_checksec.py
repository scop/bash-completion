import pytest


class TestChecksec:
    @pytest.mark.complete("checksec -")
    def test_1(self, completion):
        assert completion
