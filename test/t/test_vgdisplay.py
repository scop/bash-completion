import pytest


class TestVgdisplay:
    @pytest.mark.complete(
        "vgdisplay -", xfail="! vgdisplay --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
