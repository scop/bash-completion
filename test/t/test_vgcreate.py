import pytest


class TestVgcreate:
    @pytest.mark.complete(
        "vgcreate -", require_cmd=True, xfail="! vgcreate --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("vgcreate __does_not_exist__", require_cmd=True)
    def test_2(self, completion):
        assert not completion
