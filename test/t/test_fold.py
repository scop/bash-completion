import pytest


class TestFold:
    @pytest.mark.complete("fold --", xfail="! fold --help &>/dev/null")
    def test_1(self, completion):
        assert completion
