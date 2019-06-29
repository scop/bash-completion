import pytest


class TestVgcreate:
    @pytest.mark.complete("vgcreate -", xfail="! vgcreate --help &>/dev/null")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("vgcreate __does_not_exist__")
    def test_2(self, completion):
        assert not completion
