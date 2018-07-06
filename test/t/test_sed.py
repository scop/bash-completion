import pytest


class Test(object):

    @pytest.mark.complete("sed --",
                          skipif="! sed --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
