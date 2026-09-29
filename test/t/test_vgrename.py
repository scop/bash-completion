import pytest


class TestVgrename:
    @pytest.mark.complete(
        "vgrename -", require_cmd=True, xfail="! vgrename --help &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
