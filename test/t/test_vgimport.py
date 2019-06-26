import pytest


class TestVgimport:
    @pytest.mark.complete(
        "vgimport -", require_cmd=True, xfail="! vgimport --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
