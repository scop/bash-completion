import pytest


class TestSplit:
    @pytest.mark.complete("split --", xfail="! split --help &>/dev/null")
    def test_1(self, completion):
        assert completion
