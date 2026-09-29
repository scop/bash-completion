import pytest


class TestLvs:
    @pytest.mark.complete(
        "lvs --", require_cmd=True, xfail="! lvs --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
