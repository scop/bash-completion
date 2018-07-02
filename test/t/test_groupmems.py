import pytest


class Test(object):

    @pytest.mark.complete("groupmems -")
    def test_dash(self, completion):
        assert completion.list
