import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+_tshark_prefs=")
class TestTshark:

    @pytest.mark.complete("tshark -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tshark -G ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("tshark -O foo,htt")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("tshark -o tcp")
    def test_4(self, completion):
        assert "tcp.desegment_tcp_streams:" in completion

    @pytest.mark.complete("tshark -otcp")
    def test_5(self, completion):
        assert "-otcp.desegment_tcp_streams:" in completion
