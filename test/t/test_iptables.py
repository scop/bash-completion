import pytest


class TestIptables:
    @pytest.mark.complete("iptables -", require_cmd=True)
    def test_1(self, completion):
        assert completion
