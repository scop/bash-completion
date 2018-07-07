import pytest


class TestGperf(object):

    @pytest.mark.complete("gperf --")
    def test_1(self, completion):
        assert completion.list
