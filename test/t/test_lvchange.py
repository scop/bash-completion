import pytest


class TestLvchange:
    @pytest.mark.complete("lvchange --", xfail="! lvchange --help &>/dev/null")
    def test_1(self, completion):
        assert completion
