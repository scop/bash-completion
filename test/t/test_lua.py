import pytest


class TestLua:
    @pytest.mark.complete("lua ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lua -")
    def test_2(self, completion):
        assert completion
