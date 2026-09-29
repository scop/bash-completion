import pytest


class TestXpovray:
    @pytest.mark.complete("xpovray ")
    def test_1(self, completion):
        assert completion
