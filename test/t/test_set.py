import pytest


class TestSet:
    @pytest.mark.complete("set no")
    def test_1(self, completion):
        assert completion
