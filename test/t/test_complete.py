import pytest


class TestComplete:
    @pytest.mark.complete("complete -")
    def test_1(self, completion):
        assert completion
