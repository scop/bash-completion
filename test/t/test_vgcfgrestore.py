import pytest


class Test(object):

    @pytest.mark.complete("vgcfgrestore -",
                          skipif="! vgcfgrestore --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
