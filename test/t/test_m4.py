import pytest


class Test(object):

    @pytest.mark.complete("m4 --",
                          skipif="! m4 --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
