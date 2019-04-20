import pytest


class TestYpcat:
    @pytest.mark.complete("ypcat ")
    def test_1(self, completion):
        assert completion
