import pytest


class Test(object):

    @pytest.mark.complete("etherwake -")
    def test_dash(self, completion):
        assert completion.list
