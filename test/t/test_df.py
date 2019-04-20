import pytest


class TestDf:
    @pytest.mark.complete("df ")
    def test_1(self, completion):
        assert completion
