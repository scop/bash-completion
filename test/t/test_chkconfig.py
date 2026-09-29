import pytest


class TestChkconfig:
    @pytest.mark.complete("chkconfig -")
    def test_1(self, completion):
        assert completion

    # systemd may not be running e.g. in a docker container, and listing
    # services will then fail.
    @pytest.mark.complete(
        "chkconfig ", xfail="! systemctl list-units &>/dev/null"
    )
    def test_2(self, completion):
        assert completion
