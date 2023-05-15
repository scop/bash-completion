import pytest


class TestDcop:
    @pytest.mark.complete(
        "dcop ", require_cmd=True, skipif="! dcop &>/dev/null"
    )
    def test_1(self, completion):
        assert completion
