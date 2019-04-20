import pytest


class TestLn:
    @pytest.mark.complete("ln ")
    def test_1(self, completion):
        assert completion
