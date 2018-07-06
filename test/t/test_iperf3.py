import pytest


class Test(object):

    @pytest.mark.complete("iperf3 ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf3 --bind ")
    def test_bind(self, completion):
        assert completion.list

    @pytest.mark.complete("iperf3 --client foo --")
    def test_client(self, completion):
        assert completion.list and "--daemon" not in completion.list

    @pytest.mark.complete("iperf3 --server --")
    def test_server(self, completion):
        assert "--daemon" in completion.list
