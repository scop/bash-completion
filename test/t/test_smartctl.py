import pytest


class TestSmartctl:
    @pytest.mark.complete("smartctl --")
    def test_1(self, completion):
        assert completion
