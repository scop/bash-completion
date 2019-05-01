import pytest


class TestTouch:
    @pytest.mark.complete("touch --", xfail="! touch --help &>/dev/null")
    def test_1(self, completion):
        assert completion
