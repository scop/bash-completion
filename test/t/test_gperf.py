import pytest


class Test(object):

    @pytest.mark.complete("gperf --")
    def test_dash(self, completion):
        assert completion.list
