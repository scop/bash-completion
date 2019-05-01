import pytest


class TestUnits:
    @pytest.mark.complete("units --", xfail="! units --help &>/dev/null")
    def test_1(self, completion):
        assert completion
