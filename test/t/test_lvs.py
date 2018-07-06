import pytest


class Test(object):

    @pytest.mark.complete("lvs --",
                          skipif="! lvs --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
