import pytest


class Test(object):

    @pytest.mark.complete("vgsplit -")
    def test_dash(self, completion):
        assert completion.list
