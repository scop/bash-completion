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

    @pytest.mark.complete(
        "ip stats show group ",
        require_cmd=True,
        skipif="ip stats help 2>/dev/null; (( $? != 255 ))",
    )
    def test_stats(self, completion):
        # "link" was one of the first groups added, should always be there
        assert "link" in completion

    @pytest.mark.complete(
        "ip neigh show nud ",
        require_cmd=True,
        skipif="ip neigh help 2>&1 | grep 'STATE :=' > /dev/null; (( $? != 0 ))",
    )
    def test_neigh_state(self, completion):
        assert "stale" in completion

    @pytest.mark.complete(
        "ip monitor ",
        require_cmd=True,
        skipif="ip monitor help 2>/dev/null; (( $? != 255 ))",
    )
    def test_monitor(self, completion):
        assert "neigh" in completion
        assert "all" in completion

    @pytest.mark.complete("ip netconf ")
    def test_netconf(self, completion):
        assert "show" in completion

    @pytest.mark.complete("ip link property add ")
    def test_link_property(self, completion):
        assert "altname" in completion
        assert "dev" in completion

    @pytest.mark.complete(
        "ip addr show type ",
        require_cmd=True,
        skipif="ip link help 2>/dev/null; (( $? != 255 ))",
    )
    def test_addr_type(self, completion):
        assert "bridge" in completion

    @pytest.mark.complete("ip -", require_cmd=True)
    def test_options(self, completion):
        assert "-family" in completion
