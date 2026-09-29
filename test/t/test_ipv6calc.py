import pytest


class TestIpv6calc:
    @pytest.mark.complete("ipv6calc -", require_cmd=True)
    def test_1(self, completion):
        assert "--action" in completion

    @pytest.mark.complete("ipv6calc --in ", require_cmd=True)
    def test_2(self, completion):
        assert completion
