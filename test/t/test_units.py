import pytest


class Test(object):

    @pytest.mark.complete("units --",
                          skipif="! units --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
