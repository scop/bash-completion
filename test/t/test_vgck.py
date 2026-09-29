import pytest


class TestVgck:
    @pytest.mark.complete(
        "vgck -", require_cmd=True, xfail="! vgck --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
