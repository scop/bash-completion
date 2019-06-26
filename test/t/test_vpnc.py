import pytest


@pytest.mark.bashcomp(
    # On CentOS and Fedora, there's something fishy with consolehelper and
    # /usr/bin/vpnc going on at least when invoked as root; try to invoke the
    # one in /usr/sbin instead.
    pre_cmds=("PATH=/usr/sbin:$PATH",)
)
class TestVpnc:
    @pytest.mark.complete("vpnc -", require_cmd=True)
    def test_1(self, completion):
        assert completion
