import pytest


class TestIperf(object):

    @pytest.mark.complete("iperf ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf --bind ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf --client foo --")
    def test_3(self, completion):
        assert completion.list and "--daemon" not in completion.list

    @pytest.mark.complete("iperf --server --")
    def test_4(self, completion):
        assert "--daemon" in completion.list
