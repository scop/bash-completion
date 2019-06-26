import pytest


class TestM4:
    @pytest.mark.complete(
        "m4 --", require_cmd=True, xfail="! m4 --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
