import pytest


class TestVgextend:
    @pytest.mark.complete("vgextend -", xfail="! vgextend --help &>/dev/null")
    def test_1(self, completion):
        assert completion
