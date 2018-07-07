import pytest


class TestVgdisplay(object):

    @pytest.mark.complete("vgdisplay -",
                          skipif="! vgdisplay --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
