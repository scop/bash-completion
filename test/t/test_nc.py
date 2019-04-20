import pytest


class TestNc:
    @pytest.mark.complete("nc -")
    def test_1(self, completion):
        assert completion
