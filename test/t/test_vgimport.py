import pytest


class TestVgimport(object):

    @pytest.mark.complete("vgimport -",
                          skipif="! vgimport --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
