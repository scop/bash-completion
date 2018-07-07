import pytest


class TestVgs(object):

    @pytest.mark.complete("vgs -",
                          skipif="! vgs --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
