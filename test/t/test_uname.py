import pytest


class TestUname:
    @pytest.mark.complete("uname --", xfail="! uname --help &>/dev/null")
    def test_1(self, completion):
        assert completion
