import pytest


class TestGprof:
    @pytest.mark.complete("gprof --", xfail="! gprof --help &>/dev/null")
    def test_1(self, completion):
        assert completion
