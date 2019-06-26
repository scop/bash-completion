import pytest


class TestQuotacheck:
    @pytest.mark.complete("quotacheck -", require_cmd=True)
    def test_1(self, completion):
        assert completion
