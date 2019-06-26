import pytest


class TestVgchange:
    @pytest.mark.complete(
        "vgchange -", require_cmd=True, xfail="! vgchange --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
