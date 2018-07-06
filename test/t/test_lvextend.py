import pytest


class Test(object):

    @pytest.mark.complete("lvextend --",
                          skipif="! lvextend --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
