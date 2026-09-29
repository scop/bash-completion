import pytest


class TestSmbtree:
    @pytest.mark.complete("smbtree -", require_cmd=True)
    def test_1(self, completion):
        assert completion
