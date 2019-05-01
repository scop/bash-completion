import pytest


class TestVgcfgbackup:
    @pytest.mark.complete(
        "vgcfgbackup -", xfail="! vgcfgbackup --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
