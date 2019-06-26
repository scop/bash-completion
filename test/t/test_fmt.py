import pytest


class TestFmt:
    @pytest.mark.complete(
        "fmt -", require_cmd=True, xfail="! fmt --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
