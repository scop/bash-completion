import pytest


class TestVgcfgrestore:
    @pytest.mark.complete(
        "vgcfgrestore -", skipif="! vgcfgrestore --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
