import pytest


class TestQuotaon:
    @pytest.mark.complete("quotaon -")
    def test_1(self, completion):
        assert completion
