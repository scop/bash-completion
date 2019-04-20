import pytest


class TestIpv6calc:
    @pytest.mark.complete("ipv6calc -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ipv6calc --in ")
    def test_2(self, completion):
        assert completion
