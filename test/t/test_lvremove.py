import pytest


class TestLvremove:
    @pytest.mark.complete(
        "lvremove --", require_cmd=True, xfail="! lvremove --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lvremove /dev/map")
    def test_2(self, completion):
        assert completion == "per/"
