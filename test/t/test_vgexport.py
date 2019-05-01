import pytest


class TestVgexport:
    @pytest.mark.complete("vgexport -", xfail="! vgexport --help &>/dev/null")
    def test_1(self, completion):
        assert completion
