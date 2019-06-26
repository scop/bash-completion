import pytest


class TestFusermount:
    @pytest.mark.complete("fusermount ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("fusermount -", require_cmd=True)
    def test_2(self, completion):
        assert completion
