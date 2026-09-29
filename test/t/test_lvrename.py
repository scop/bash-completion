import pytest


class TestLvrename:
    @pytest.mark.complete(
        "lvrename --", require_cmd=True, xfail="! lvrename --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
