import pytest


class Test(object):

    @pytest.mark.complete("uname --",
                          skipif="! uname --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
