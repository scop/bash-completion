import pytest


class TestIwspy:
    @pytest.mark.complete("iwspy --")
    def test_1(self, completion):
        assert completion
