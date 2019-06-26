import pytest


class TestLvextend:
    @pytest.mark.complete(
        "lvextend --", require_cmd=True, xfail="! lvextend --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
