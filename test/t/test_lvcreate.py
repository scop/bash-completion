import pytest


class Test(object):

    @pytest.mark.complete("lvcreate --",
                          skipif="! lvcreate --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
