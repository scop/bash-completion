import pytest


class TestIpsec:
    @pytest.mark.complete("ipsec ")
    def test_1(self, completion):
        assert completion
