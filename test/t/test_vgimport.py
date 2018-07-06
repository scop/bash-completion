import pytest


class Test(object):

    @pytest.mark.complete("vgimport -",
                          skipif="! vgimport --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
