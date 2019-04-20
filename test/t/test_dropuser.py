import pytest


class TestDropuser:
    @pytest.mark.complete("dropuser ")
    def test_1(self, completion):
        assert completion
