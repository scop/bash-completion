import pytest


class TestPvdisplay(object):

    @pytest.mark.complete("pvdisplay --",
                          skipif="! pvdisplay --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
