import pytest


class TestVgmknodes:
    @pytest.mark.complete(
        "vgmknodes -", require_cmd=True, xfail="! vgmknodes --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
