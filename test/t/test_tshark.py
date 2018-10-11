import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+_tshark_pr(ef|otocol)s=")
class TestTshark:
    @pytest.mark.complete("tshark -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tshark -G ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("tshark -O foo,htt")
    def test_3(self, completion):
        # When there's only one completion, it's be the one with "foo," prefix;
        # when multiple (e.g. http and http2), it's the completion alone.
        assert completion == "foo,http" or "http" in completion

    @pytest.mark.complete("tshark -o tcp")
    def test_4(self, completion):
        assert "tcp.desegment_tcp_streams:" in completion

    @pytest.mark.complete("tshark -otcp")
    def test_5(self, completion):
        assert "-otcp.desegment_tcp_streams:" in completion

    @pytest.mark.complete("tshark -O http")
    def test_6(self, completion):
        """Test there are no URLs in completions."""
        assert not any("://" in x for x in completion)
