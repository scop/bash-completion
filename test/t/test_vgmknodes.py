import pytest


class Test(object):

    @pytest.mark.complete("vgmknodes -",
                          skipif="! vgmknodes --help &>/dev/null")
    def test_(self, completion):
        assert completion.list
