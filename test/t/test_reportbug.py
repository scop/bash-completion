import pytest


class TestReportbug:
    @pytest.mark.complete("reportbug --m", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("reportbug --bts=", require_cmd=True)
    def test_bts(self, completion):
        assert "default" in completion
