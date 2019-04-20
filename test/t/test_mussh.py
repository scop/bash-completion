import pytest


class TestMussh:
    @pytest.mark.complete("mussh -")
    def test_1(self, completion):
        assert completion
