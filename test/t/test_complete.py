import pytest


class TestComplete:
    @pytest.mark.complete("complete -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(r"\complete -")
    def test_2(self, completion):
        assert completion
