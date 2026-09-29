import pytest

from conftest import assert_bash_exec


class TestNmap:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(bash, "_mock_nmap() { cat nmap/nmap-h.txt; }")
        assert_bash_exec(bash, "complete -F _comp_cmd_nmap _mock_nmap")

    @pytest.mark.complete("nmap --v", require_cmd=True)
    def test_live_options(self, completion):
        assert completion

    @pytest.mark.complete("nmap ")
    def test_hosts(self, completion):
        assert completion

    @pytest.mark.complete("_mock_nmap -")
    def test_mock_options(self, completion, functions):
        assert completion == sorted(
            "-iL -iR --exclude --excludefile -sL -sn -Pn -PS -PA -PU -PY -PE "
            "-PP -PM -PO -n -R --dns-servers --system-dns --traceroute -sS "
            "-sT -sA -sW -sM -sU -sN -sF -sX --scanflags -sI -sY -sZ -sO -b "
            "-p --exclude-ports -F -r --top-ports --port-ratio -sV "
            "--version-intensity --version-light --version-all "
            "--version-trace -sC --script= --script-args= --script-args-file= "
            "--script-trace --script-updatedb --script-help= -O "
            "--osscan-limit --osscan-guess "
            # TODO: -T known mishandled; should expand -T<0-5> to -T0 ... -T5
            "-T --min-hostgroup --max-hostgroup --min-parallelism "
            "--max-parallelism --min-rtt-timeout --max-rtt-timeout "
            "--initial-rtt-timeout --max-retries --host-timeout --scan-delay "
            "--max-scan-delay --min-rate --max-rate -f --mtu -D -S -e -g "
            "--source-port --proxies --data --data-string --data-length "
            "--ip-options --ttl --spoof-mac --badsum -oN -oX -oS -oG -oA -v "
            "-d --reason --open --packet-trace --iflist --append-output "
            "--resume --stylesheet --webxml --no-stylesheet -6 -A --datadir "
            "--send-eth --send-ip --privileged --unprivileged -V -h"
            "".strip().split()
        )

    @pytest.mark.complete("_mock_nmap --script-args-f")
    def test_mock_nospace(self, completion, functions):
        assert completion == "ile="
        assert completion.endswith("=")  # no space appended
