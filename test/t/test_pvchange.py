import pytest


class Test(object):

    @pytest.mark.complete("pvchange --",
                          skipif="! pvchange --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
