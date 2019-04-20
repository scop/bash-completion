import pytest


class TestLuac:
    @pytest.mark.complete("luac ")
    def test_1(self, completion):
        assert completion
