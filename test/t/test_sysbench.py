import pytest


class TestSysbench:
    @pytest.mark.complete("sysbench ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sysbench -")
    def test_2(self, completion):
        assert completion
