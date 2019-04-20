import pytest


class TestQuotacheck:
    @pytest.mark.complete("quotacheck -")
    def test_1(self, completion):
        assert completion
