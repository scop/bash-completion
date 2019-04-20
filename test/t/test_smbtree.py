import pytest


class TestSmbtree:
    @pytest.mark.complete("smbtree -")
    def test_1(self, completion):
        assert completion
