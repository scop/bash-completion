import pytest


class TestHtop:
    @pytest.mark.complete("htop -")
    def test_1(self, completion):
        assert completion
