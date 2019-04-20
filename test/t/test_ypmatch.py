import pytest


class TestYpmatch:
    @pytest.mark.complete("ypmatch foo ")
    def test_1(self, completion):
        assert completion
