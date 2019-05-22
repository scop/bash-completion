import pytest


class TestSysctl:
    @pytest.mark.complete("sysctl -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "sysctl kern",
        xfail="! sysctl -N -a 2>/dev/null | command grep -q ^kern",
    )
    def test_2(self, completion):
        assert completion
