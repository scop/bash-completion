import pytest


class Test(object):

    @pytest.mark.complete("who --",
                          skipif="! who --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
