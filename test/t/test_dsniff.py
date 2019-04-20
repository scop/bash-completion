import pytest


class TestDsniff:
    @pytest.mark.complete("dsniff -")
    def test_1(self, completion):
        assert completion
