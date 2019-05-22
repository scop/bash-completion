import pytest


class TestLvscan:
    @pytest.mark.complete("lvscan --", xfail="! lvscan --help &>/dev/null")
    def test_1(self, completion):
        assert completion
