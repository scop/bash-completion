import pytest


class Test(object):

    @pytest.mark.complete("phing -")
    def test_dash(self, completion):
        assert completion.list
