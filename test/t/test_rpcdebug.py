import pytest


class Test(object):

    @pytest.mark.complete("rpcdebug -")
    def test_dash(self, completion):
        assert completion.list
