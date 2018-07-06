import pytest


class Test(object):

    @pytest.mark.complete("pvcreate --",
                          skipif="! pvcreate --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
