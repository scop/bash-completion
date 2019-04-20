import pytest


class TestRmmod:
    @pytest.mark.complete("rmmod -")
    def test_1(self, completion):
        assert completion
