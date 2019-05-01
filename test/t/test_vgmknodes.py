import pytest


class TestVgmknodes:
    @pytest.mark.complete(
        "vgmknodes -", xfail="! vgmknodes --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
