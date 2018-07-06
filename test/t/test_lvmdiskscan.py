import pytest


class Test(object):

    @pytest.mark.complete("lvmdiskscan --",
                          skipif="! lvmdiskscan --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
