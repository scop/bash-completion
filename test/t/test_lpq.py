import pytest


class TestLpq:
    @pytest.mark.complete("lpq ")
    def test_1(self, completion):
        assert completion
