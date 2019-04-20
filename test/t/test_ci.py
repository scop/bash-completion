import pytest


class TestCi:
    @pytest.mark.complete("ci ")
    def test_1(self, completion):
        assert completion
