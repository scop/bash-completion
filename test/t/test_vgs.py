import pytest


class TestVgs:
    @pytest.mark.complete("vgs -", skipif="! vgs --help &>/dev/null")
    def test_1(self, completion):
        assert completion
