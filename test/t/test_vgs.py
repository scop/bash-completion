import pytest


class TestVgs:
    @pytest.mark.complete("vgs -", xfail="! vgs --help &>/dev/null")
    def test_1(self, completion):
        assert completion
