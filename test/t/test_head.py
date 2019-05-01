import pytest


class TestHead:
    @pytest.mark.complete("head --", xfail="! head --help &>/dev/null")
    def test_1(self, completion):
        assert completion
