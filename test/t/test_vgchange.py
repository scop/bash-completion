import pytest


class Test(object):

    @pytest.mark.complete("vgchange -")
    def test_dash(self, completion):
        assert completion.list
