import pytest


class TestGenisoimage:
    @pytest.mark.complete("genisoimage ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("genisoimage -", require_cmd=True)
    def test_2(self, completion):
        assert completion
