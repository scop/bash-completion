import pytest


class TestLvcreate:
    @pytest.mark.complete("lvcreate --", xfail="! lvcreate --help &>/dev/null")
    def test_1(self, completion):
        assert completion
