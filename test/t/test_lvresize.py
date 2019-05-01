import pytest


class TestLvresize:
    @pytest.mark.complete("lvresize --", xfail="! lvresize --help &>/dev/null")
    def test_1(self, completion):
        assert completion
