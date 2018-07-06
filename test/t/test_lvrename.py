import pytest


class Test(object):

    @pytest.mark.complete("lvrename --",
                          skipif="! lvrename --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
