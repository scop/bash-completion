import pytest


class TestDisplay:
    @pytest.mark.complete("display ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("display -")
    def test_2(self, completion):
        assert completion
