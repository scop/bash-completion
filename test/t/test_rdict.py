import pytest


class TestRdict:
    @pytest.mark.complete("rdict --")
    def test_1(self, completion):
        assert completion
