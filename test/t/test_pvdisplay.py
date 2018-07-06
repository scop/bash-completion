import pytest


class Test(object):

    @pytest.mark.complete("pvdisplay --",
                          skipif="! pvdisplay --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
