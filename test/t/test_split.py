import pytest


class TestSplit:

    @pytest.mark.complete("split --",
                          skipif="! split --help &>/dev/null")
    def test_1(self, completion):
        assert completion
