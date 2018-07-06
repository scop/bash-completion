import pytest


class Test(object):

    @pytest.mark.complete("head --",
                          skipif="! head --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
