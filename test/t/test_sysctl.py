import pytest


class TestSysctl:
    @pytest.mark.complete("sysctl -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "sysctl kern",
        require_cmd=True,
        xfail="! sysctl -N -a 2>/dev/null | command grep -q ^kern",
    )
    def test_2(self, completion):
        assert completion
