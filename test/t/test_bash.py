import pytest


class TestBash:
    @pytest.mark.complete("bash --")
    def test_1(self, completion):
        assert completion
