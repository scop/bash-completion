import pytest


class Test(object):

    @pytest.mark.complete("env --",
                          skipif="! env --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
