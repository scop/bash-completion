import pytest


class Test(object):

    @pytest.mark.complete("lvdisplay --",
                          skipif="! lvdisplay --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
