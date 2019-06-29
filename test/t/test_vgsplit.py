import pytest


class TestVgsplit:
    @pytest.mark.complete("vgsplit -", xfail="! vgsplit --help &>/dev/null")
    def test_1(self, completion):
        assert completion
