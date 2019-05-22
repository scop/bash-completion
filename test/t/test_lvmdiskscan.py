import pytest


class TestLvmdiskscan:
    @pytest.mark.complete(
        "lvmdiskscan --", xfail="! lvmdiskscan --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
