import pytest


class TestVgck:
    @pytest.mark.complete("vgck -", xfail="! vgck --help &>/dev/null")
    def test_1(self, completion):
        assert completion
