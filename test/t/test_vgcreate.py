import pytest


class TestVgcreate:
    @pytest.mark.complete("vgcreate -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("vgcreate __does_not_exist__")
    def test_2(self, completion):
        assert not completion
