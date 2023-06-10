import pytest


class TestLvm:
    @pytest.mark.complete("lvm pv")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "lvm lvcreate --",
        require_cmd=True,
        xfail="! lvm lvcreate --help &>/dev/null",
    )
    def test_subcommand_options(self, completion):
        assert completion
