import pytest


class TestSysbench:
    @pytest.mark.complete("sysbench ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sysbench -", require_cmd=True)
    def test_2(self, completion):
        assert completion
