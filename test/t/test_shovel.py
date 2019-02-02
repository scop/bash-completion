import pytest


class TestShovel:

    @pytest.mark.complete("shovel ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("shovel --")
    def test_2(self, completion):
        assert completion
