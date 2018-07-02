import pytest


class Test(object):

    @pytest.mark.complete("eject -")
    def test_dash(self, completion):
        assert completion.list
