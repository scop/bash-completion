import pytest


class TestLsusb:
    @pytest.mark.complete(
        "lsusb -",
        xfail="! (lsusb --help 2>&1 || :) | command grep -qF -- --help",
    )
    def test_1(self, completion):
        assert completion
