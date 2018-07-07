import pytest


class TestLvmdiskscan(object):

    @pytest.mark.complete("lvmdiskscan --",
                          skipif="! lvmdiskscan --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
