import pytest


class TestMc:
    @pytest.mark.complete("mc -")
    def test_1(self, completion):
        assert completion
