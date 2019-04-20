import pytest


class TestPatch:
    @pytest.mark.complete("patch ")
    def test_1(self, completion):
        assert completion
