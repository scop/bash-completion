import pytest


class TestPvs:
    @pytest.mark.complete("pvs --", xfail="! pvs --help &>/dev/null")
    def test_1(self, completion):
        assert completion
