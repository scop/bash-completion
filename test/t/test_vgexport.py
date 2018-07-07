import pytest


class TestVgexport(object):

    @pytest.mark.complete("vgexport -",
                          skipif="! vgexport --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
