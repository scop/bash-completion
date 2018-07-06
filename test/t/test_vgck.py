import pytest


class Test(object):

    @pytest.mark.complete("vgck -",
                          skipif="! vgck --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
