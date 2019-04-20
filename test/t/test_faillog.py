import pytest


class TestFaillog:
    @pytest.mark.complete("faillog -")
    def test_1(self, completion):
        assert completion
