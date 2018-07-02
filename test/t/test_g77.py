import pytest


class Test(object):

    @pytest.mark.complete("g77 ")
    def test_(self, completion):
        assert completion.list
