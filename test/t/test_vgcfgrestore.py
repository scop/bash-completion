import pytest


class TestVgcfgrestore:
    @pytest.mark.complete(
        "vgcfgrestore -", xfail="! vgcfgrestore --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
