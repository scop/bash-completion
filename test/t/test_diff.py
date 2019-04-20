import pytest


class TestDiff:
    @pytest.mark.complete("diff --")
    def test_1(self, completion):
        assert completion
