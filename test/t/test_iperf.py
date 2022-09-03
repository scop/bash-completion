import pytest


class TestIperf:
    @pytest.mark.complete("iperf ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("iperf --bind ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("iperf --client foo --", require_cmd=True)
    def test_3(self, completion):
        assert completion
        assert "--daemon" not in completion

    @pytest.mark.complete("iperf --server --", require_cmd=True)
    def test_4(self, completion):
        assert "--daemon" in completion

    @pytest.mark.complete("iperf -", require_cmd=True)
    def test_5(self, completion):
        assert completion

    @pytest.mark.complete("iperf --format ", require_cmd=True)
    def test_format(self, completion):
        # 2.0.5 has only up to m/M, later may have g/G, t/T, ...
        assert all(x in completion for x in "k m K M".split())
