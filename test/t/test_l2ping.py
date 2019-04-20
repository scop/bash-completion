import pytest


class TestL2ping:
    @pytest.mark.complete("l2ping -")
    def test_1(self, completion):
        assert completion
