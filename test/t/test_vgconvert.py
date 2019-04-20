import pytest


class TestVgconvert:
    @pytest.mark.complete(
        "vgconvert -", skipif="! vgconvert --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
