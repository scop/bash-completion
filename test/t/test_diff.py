import pytest


class TestDiff:
    @pytest.mark.complete("diff --", require_cmd=True)
    def test_1(self, completion):
        assert completion
