import pytest


class Test(object):

    @pytest.mark.complete("vgcfgbackup -",
                          skipif="! vgcfgbackup --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
