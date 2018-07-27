import pytest


class TestGenisoimage:

    @pytest.mark.complete("genisoimage ")
    def test_1(self, completion):
        assert completion.list
