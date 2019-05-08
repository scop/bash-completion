import pytest


class TestBadblocks:
    @pytest.mark.complete("badblocks ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("badblocks -")
    def test_2(self, completion):
        assert completion
