import pytest


class TestVgremove:
    @pytest.mark.complete(
        "vgremove -", require_cmd=True, xfail="! vgremove --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
