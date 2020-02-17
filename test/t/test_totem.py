import pytest


class TestTotem:
    @pytest.mark.complete("totem ")
    def test_basic(self, completion):
        assert completion
