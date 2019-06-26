import pytest


class TestLvremove:
    @pytest.mark.complete(
        "lvremove --", require_cmd=True, xfail="! lvremove --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
