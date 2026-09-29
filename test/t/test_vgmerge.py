import pytest


class TestVgmerge:
    @pytest.mark.complete(
        "vgmerge -", require_cmd=True, xfail="! vgmerge --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
