import pytest


class Test(object):

    @pytest.mark.complete("split --",
                          skipif="! split --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
