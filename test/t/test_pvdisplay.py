import pytest


class TestPvdisplay:
    @pytest.mark.complete(
        "pvdisplay --",
        require_cmd=True,
        xfail="! pvdisplay --help &>/dev/null",
    )
    def test_1(self, completion):
        assert completion
