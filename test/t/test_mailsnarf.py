import pytest


class TestMailsnarf:
    @pytest.mark.complete("mailsnarf -")
    def test_1(self, completion):
        assert completion
