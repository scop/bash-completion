import pytest


class Test(object):

    @pytest.mark.complete("iwspy --")
    def test_dash(self, completion):
        assert completion.list
