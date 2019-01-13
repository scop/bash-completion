import pytest


class TestBadblocks:

    @pytest.mark.complete("badblocks ")
    def test_1(self, completion):
        assert completion
