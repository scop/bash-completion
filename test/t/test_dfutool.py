import pytest


class TestDfutool:
    @pytest.mark.complete("dfutool ")
    def test_1(self, completion):
        assert completion
