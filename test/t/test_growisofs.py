import pytest


class TestGrowisofs:
    @pytest.mark.complete("growisofs ")
    def test_1(self, completion):
        assert completion
