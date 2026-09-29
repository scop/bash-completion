import pytest


class TestQuotaon:
    @pytest.mark.complete("quotaon -", require_cmd=True)
    def test_1(self, completion):
        assert completion
