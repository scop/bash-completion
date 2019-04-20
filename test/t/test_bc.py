import pytest


class TestBc:
    @pytest.mark.complete("bc --")
    def test_1(self, completion):
        assert completion
