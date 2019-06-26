import pytest


class TestVgexport:
    @pytest.mark.complete(
        "vgexport -", require_cmd=True, xfail="! vgexport --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
