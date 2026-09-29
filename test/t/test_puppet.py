import pytest


class TestPuppet:
    @pytest.mark.complete("puppet ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("puppet agent --")
    def test_2(self, completion):
        assert completion
