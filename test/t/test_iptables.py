import pytest


class TestIptables:
    @pytest.mark.complete("iptables -")
    def test_1(self, completion):
        assert completion
