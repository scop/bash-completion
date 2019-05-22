import pytest


class TestLvdisplay:
    @pytest.mark.complete(
        "lvdisplay --", xfail="! lvdisplay --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
