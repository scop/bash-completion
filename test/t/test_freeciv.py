import pytest


class TestFreeciv:
    @pytest.mark.complete("freeciv -")
    def test_1(self, completion):
        assert completion
