import pytest


class TestVgcfgrestore:
    @pytest.mark.complete(
        "vgcfgrestore -",
        require_cmd=True,
        xfail="! vgcfgrestore --help &>/dev/null",
    )
    def test_1(self, completion):
        assert completion
