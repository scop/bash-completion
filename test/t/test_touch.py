import pytest


class Test(object):

    @pytest.mark.complete("touch --",
                          skipif="! touch --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
