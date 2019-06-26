import pytest


class TestFreeciv:
    @pytest.mark.complete("freeciv -", require_cmd=True)
    def test_1(self, completion):
        assert completion
