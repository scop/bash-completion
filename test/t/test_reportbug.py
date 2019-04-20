import pytest


class TestReportbug:
    @pytest.mark.complete("reportbug --m")
    def test_1(self, completion):
        assert completion
