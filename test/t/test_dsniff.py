import pytest


class Test(object):

    @pytest.mark.complete("dsniff -")
    def test_dash(self, completion):
        assert completion.list
