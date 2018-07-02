import pytest


class Test(object):

    @pytest.mark.complete("jps -")
    def test_dash(self, completion):
        assert completion.list
