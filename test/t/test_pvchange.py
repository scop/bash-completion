import pytest


class TestPvchange:
    @pytest.mark.complete(
        "pvchange --", require_cmd=True, xfail="! pvchange --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
