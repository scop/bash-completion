import pytest


class Test(object):

    @pytest.mark.complete("resolvconf -")
    def test_dash(self, completion):
        assert completion.list
