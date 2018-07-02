import pytest


class Test(object):

    @pytest.mark.complete("clone_member -")
    def test_dash(self, completion):
        assert completion.list
