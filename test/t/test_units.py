import pytest


class TestUnits:
    @pytest.mark.complete(
        "units --", require_cmd=True, xfail="! units --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
