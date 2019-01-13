import pytest


class TestSysbench:

    @pytest.mark.complete("sysbench ")
    def test_1(self, completion):
        assert completion
