import pytest


class Test(object):

    @pytest.mark.complete("lvresize --",
                          skipif="! lvresize --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
