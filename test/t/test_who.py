import pytest


class TestWho:
    @pytest.mark.complete("who --", xfail="! who --help &>/dev/null")
    def test_1(self, completion):
        assert completion
