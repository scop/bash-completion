import pytest


class TestLvdisplay:
    @pytest.mark.complete(
        "lvdisplay --",
        require_cmd=True,
        xfail="! lvdisplay --help &>/dev/null",
    )
    def test_1(self, completion):
        assert completion
