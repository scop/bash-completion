import pytest


class TestMtx:
    @pytest.mark.complete("mtx ")
    def test_1(self, completion):
        assert completion
