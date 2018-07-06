import pytest


class Test(object):

    @pytest.mark.complete("vgreduce -",
                          skipif="! vgreduce --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
