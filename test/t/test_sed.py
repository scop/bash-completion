import pytest


class TestSed:
    @pytest.mark.complete("sed --", xfail="! sed --help &>/dev/null")
    def test_1(self, completion):
        assert completion
