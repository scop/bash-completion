import pytest


class TestVgs:
    @pytest.mark.complete(
        "vgs -", require_cmd=True, xfail="! vgs --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
