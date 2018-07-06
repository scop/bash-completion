import pytest


class Test(object):

    @pytest.mark.complete("vgconvert -",
                          skipif="! vgconvert --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
