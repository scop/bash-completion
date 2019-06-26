import pytest


class TestPvcreate:
    @pytest.mark.complete(
        "pvcreate --", require_cmd=True, xfail="! pvcreate --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
