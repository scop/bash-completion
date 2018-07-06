import pytest


class Test(object):

    @pytest.mark.complete("vgextend -",
                          skipif="! vgextend --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
