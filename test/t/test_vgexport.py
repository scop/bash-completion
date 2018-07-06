import pytest


class Test(object):

    @pytest.mark.complete("vgexport -",
                          skipif="! vgexport --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
