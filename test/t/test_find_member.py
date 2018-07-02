import pytest


class Test(object):

    @pytest.mark.complete("find_member -")
    def test_dash(self, completion):
        assert completion.list
