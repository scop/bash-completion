import pytest


class TestPvmove:
    @pytest.mark.complete("pvmove --", xfail="! pvmove --help &>/dev/null")
    def test_1(self, completion):
        assert completion
