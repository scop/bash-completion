import pytest


class Test(object):

    @pytest.mark.complete("list_lists -")
    def test_dash(self, completion):
        assert completion.list
