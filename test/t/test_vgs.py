import pytest


class Test(object):

    @pytest.mark.complete("vgs -",
                          skipif="! vgs --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
