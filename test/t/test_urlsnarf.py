import pytest


class TestUrlsnarf:
    @pytest.mark.complete("urlsnarf -")
    def test_1(self, completion):
        assert completion
