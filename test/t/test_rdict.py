import pytest


class TestRdict:
    @pytest.mark.complete("rdict --", require_cmd=True)
    def test_1(self, completion):
        assert completion
