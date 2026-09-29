import pytest


class TestCompare:
    @pytest.mark.complete("compare ")
    def test_1(self, completion):
        assert completion
