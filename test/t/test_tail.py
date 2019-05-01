import pytest


class TestTail:
    @pytest.mark.complete("tail --", xfail="! tail --help &>/dev/null")
    def test_1(self, completion):
        assert completion
