import pytest


class TestDict:
    @pytest.mark.complete("dict -")
    def test_1(self, completion):
        assert completion
