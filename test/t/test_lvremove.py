import pytest


class TestLvremove:
    @pytest.mark.complete("lvremove --", xfail="! lvremove --help &>/dev/null")
    def test_1(self, completion):
        assert completion
