import pytest


class TestOd:
    @pytest.mark.complete("od ")
    def test_1(self, completion):
        assert completion
