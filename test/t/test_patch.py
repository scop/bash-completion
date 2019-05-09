import pytest


class TestPatch:
    @pytest.mark.complete("patch ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("patch -")
    def test_2(self, completion):
        assert completion
