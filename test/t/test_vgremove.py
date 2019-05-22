import pytest


class TestVgremove:
    @pytest.mark.complete("vgremove -", xfail="! vgremove --help &>/dev/null")
    def test_1(self, completion):
        assert completion
