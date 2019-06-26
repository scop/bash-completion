import pytest


class TestWho:
    @pytest.mark.complete(
        "who --", require_cmd=True, xfail="! who --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
