import pytest


class Test(object):

    @pytest.mark.complete("iwconfig --")
    def test_dash(self, completion):
        assert completion.list
