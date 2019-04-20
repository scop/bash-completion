import pytest


class TestDate:
    @pytest.mark.complete("date ")
    def test_1(self, completion):
        assert completion
