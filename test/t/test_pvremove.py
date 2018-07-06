import pytest


class Test(object):

    @pytest.mark.complete("pvremove --",
                          skipif="! pvremove --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
