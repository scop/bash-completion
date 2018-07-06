import pytest


class Test(object):

    @pytest.mark.complete("lvremove --",
                          skipif="! lvremove --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
