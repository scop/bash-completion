import pytest


class TestG4:
    @pytest.mark.complete("g4 ")
    def test_1(self, completion):
        assert completion
