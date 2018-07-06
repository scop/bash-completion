import pytest


class Test(object):

    @pytest.mark.complete("vgdisplay -",
                          skipif="! vgdisplay --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
