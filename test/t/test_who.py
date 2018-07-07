import pytest


class TestWho(object):

    @pytest.mark.complete("who --",
                          skipif="! who --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
