import pytest


class Test(object):

    @pytest.mark.complete("lastlog -")
    def test_dash(self, completion):
        assert completion.list
