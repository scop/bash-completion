import pytest


class TestDot:
    @pytest.mark.complete("dot ")
    def test_1(self, completion):
        assert completion
