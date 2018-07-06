import pytest


class Test(object):

    @pytest.mark.complete("expand --",
                          skipif="! expand --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
