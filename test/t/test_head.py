import pytest


class TestHead:

    @pytest.mark.complete("head --",
                          skipif="! head --help &>/dev/null")
    def test_1(self, completion):
        assert completion
