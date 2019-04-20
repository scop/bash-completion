import pytest


class TestTee:
    @pytest.mark.complete("tee ")
    def test_1(self, completion):
        assert completion
