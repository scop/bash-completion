import pytest


class TestQuota:
    @pytest.mark.complete("quota ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("quota -")
    def test_2(self, completion):
        assert completion
