import pytest


class TestLvcreate:
    @pytest.mark.complete(
        "lvcreate --", require_cmd=True, xfail="! lvcreate --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
