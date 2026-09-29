import pytest


class TestLspci:
    @pytest.mark.complete("lspci -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "lspci -A ", require_cmd=True, skipif="! lspci -A help &>/dev/null"
    )
    def test_2(self, completion):
        assert completion
