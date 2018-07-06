import pytest


class Test(object):

    @pytest.mark.complete("uniq --",
                          skipif="! uniq --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
