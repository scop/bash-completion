import pytest


class TestVgextend(object):

    @pytest.mark.complete("vgextend -",
                          skipif="! vgextend --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
