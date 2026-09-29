import pytest


class TestLvscan:
    @pytest.mark.complete(
        "lvscan --", require_cmd=True, xfail="! lvscan --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
