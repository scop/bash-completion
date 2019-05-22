import pytest


class TestPvdisplay:
    @pytest.mark.complete(
        "pvdisplay --", xfail="! pvdisplay --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
