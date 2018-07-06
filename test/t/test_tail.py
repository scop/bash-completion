import pytest


class Test(object):

    @pytest.mark.complete("tail --",
                          skipif="! tail --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
