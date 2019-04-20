import pytest


class TestIperf3:
    @pytest.mark.complete("iperf3 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("iperf3 --bind ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("iperf3 --client foo --")
    def test_3(self, completion):
        assert completion
        assert "--daemon" not in completion

    @pytest.mark.complete("iperf3 --server --")
    def test_4(self, completion):
        assert "--daemon" in completion
