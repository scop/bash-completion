import pytest


class TestConjure:
    @pytest.mark.complete("conjure ")
    def test_1(self, completion):
        assert completion
