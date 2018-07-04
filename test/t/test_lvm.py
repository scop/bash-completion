import pytest


class Test(object):

    @pytest.mark.complete("lvm pv")
    def test_pv(self, completion):
        assert completion.list
