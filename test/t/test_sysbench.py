import pytest


class TestSysbench(object):

    @pytest.mark.complete("sysbench ")
    def test_1(self, completion):
        assert completion.list
