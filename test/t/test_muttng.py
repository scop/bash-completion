import pytest


class TestMuttng:
    @pytest.mark.complete("muttng -")
    def test_1(self, completion):
        assert completion
