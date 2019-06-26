import pytest


class TestVgscan:
    @pytest.mark.complete(
        "vgscan -", require_cmd=True, xfail="! vgscan --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
