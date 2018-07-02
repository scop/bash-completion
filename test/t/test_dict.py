import pytest


class Test(object):

    @pytest.mark.complete("dict -")
    def test_dash(self, completion):
        assert completion.list
