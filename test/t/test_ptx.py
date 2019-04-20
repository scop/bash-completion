import pytest


class TestPtx:
    @pytest.mark.complete("ptx ")
    def test_1(self, completion):
        assert completion
