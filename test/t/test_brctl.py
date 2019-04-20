import pytest


class TestBrctl:
    @pytest.mark.complete("brctl ")
    def test_1(self, completion):
        assert completion
