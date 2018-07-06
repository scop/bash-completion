import pytest


class Test(object):

    @pytest.mark.complete("wc --",
                          skipif="! wc --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
