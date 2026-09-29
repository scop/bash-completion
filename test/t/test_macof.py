import pytest


class TestMacof:
    @pytest.mark.complete("macof -", require_cmd=True)
    def test_1(self, completion):
        assert completion
