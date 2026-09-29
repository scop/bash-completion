import pytest


class TestPovray:
    @pytest.mark.complete("povray ")
    def test_1(self, completion):
        assert completion
