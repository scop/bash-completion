import pytest


class TestWc:
    @pytest.mark.complete("wc --", xfail="! wc --help &>/dev/null")
    def test_1(self, completion):
        assert completion
