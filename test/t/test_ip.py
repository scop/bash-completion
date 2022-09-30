import pytest


class TestIp:
    @pytest.mark.complete("ip ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ip a ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("ip route replace ", require_cmd=True)
    def test_r_r(self, completion):
        assert completion

    @pytest.mark.complete("ip -", require_cmd=True)
    def test_options(self, completion):
        assert "-family" in completion
