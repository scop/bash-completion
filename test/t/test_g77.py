import pytest


class TestG77:
    @pytest.mark.complete("g77 ")
    def test_1(self, completion):
        assert completion
