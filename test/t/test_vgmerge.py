import pytest


class Test(object):

    @pytest.mark.complete("vgmerge -",
                          skipif="! vgmerge --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
