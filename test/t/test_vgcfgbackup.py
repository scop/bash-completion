import pytest


class TestVgcfgbackup:
    @pytest.mark.complete(
        "vgcfgbackup -",
        require_cmd=True,
        xfail="! vgcfgbackup --help &>/dev/null",
    )
    def test_1(self, completion):
        assert completion
