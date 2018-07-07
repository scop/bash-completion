import pytest


class TestReportbug(object):

    @pytest.mark.complete("reportbug --m")
    def test_1(self, completion):
        assert completion.list
