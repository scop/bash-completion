import pytest


class Test(object):

    @pytest.mark.complete("civclient -")
    def test_dash(self, completion):
        assert completion.list
