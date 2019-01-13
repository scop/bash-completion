import pytest


class TestWho:

    @pytest.mark.complete("who --",
                          skipif="! who --help &>/dev/null")
    def test_1(self, completion):
        assert completion
