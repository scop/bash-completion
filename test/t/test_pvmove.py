import pytest


class TestPvmove:
    @pytest.mark.complete(
        "pvmove --", require_cmd=True, xfail="! pvmove --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
