import pytest


class TestUscan:
    @pytest.mark.complete("uscan -")
    def test_1(self, completion):
        assert completion
