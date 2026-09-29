import pytest


class TestUscan:
    @pytest.mark.complete("uscan -", require_cmd=True)
    def test_1(self, completion):
        assert completion
