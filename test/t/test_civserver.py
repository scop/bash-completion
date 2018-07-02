import pytest


class Test(object):

    @pytest.mark.complete("civserver -")
    def test_dash(self, completion):
        assert completion.list
