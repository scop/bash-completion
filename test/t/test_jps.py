import pytest


class TestJps:
    @pytest.mark.complete("jps -")
    def test_1(self, completion):
        assert completion
