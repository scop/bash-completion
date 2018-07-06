import pytest


class Test(object):

    @pytest.mark.complete("lvscan --",
                          skipif="! lvscan --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
