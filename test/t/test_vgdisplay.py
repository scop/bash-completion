import pytest


class TestVgdisplay:
    @pytest.mark.complete(
        "vgdisplay -", require_cmd=True, xfail="! vgdisplay --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
