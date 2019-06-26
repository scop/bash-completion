import pytest


class TestReportbug:
    @pytest.mark.complete("reportbug --m", require_cmd=True)
    def test_1(self, completion):
        assert completion
