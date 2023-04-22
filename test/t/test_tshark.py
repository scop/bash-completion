import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+_comp_cmd_tshark__pr(ef|otocol)s=")
class TestTshark:
    @pytest.mark.complete("tshark -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tshark -G ", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("tshark -O foo,htt", require_cmd=True)
    def test_3(self, completion):
        # p: one completion only; http: e.g. http and http2
        assert completion == "p" or "foo,http" in completion

    @pytest.mark.complete("tshark -o tcp", require_cmd=True)
    def test_4(self, completion):
        assert "tcp.desegment_tcp_streams:" in completion

    @pytest.mark.complete("tshark -otcp", require_cmd=True)
    def test_5(self, completion):
        assert "-otcp.desegment_tcp_streams:" in completion

    @pytest.mark.complete("tshark -O http")
    def test_6(self, completion):
        """Test there are no URLs in completions."""
        assert not any("://" in x for x in completion)

    @pytest.mark.complete("tshark -r ")
    def test_input_files(self, completion):
        assert completion
