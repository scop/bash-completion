import pytest


class TestChecksec:
    @pytest.mark.complete("checksec -", require_cmd=True)
    def test_1(self, completion):
        assert completion
