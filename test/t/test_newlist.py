import pytest


class TestNewlist:
    @pytest.mark.complete("newlist -")
    def test_1(self, completion):
        assert completion
