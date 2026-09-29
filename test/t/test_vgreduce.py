import pytest


class TestVgreduce:
    @pytest.mark.complete(
        "vgreduce -", require_cmd=True, xfail="! vgreduce --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
