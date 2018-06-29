import pytest


class Test(object):

    @pytest.mark.complete("rdict --")
    def test_dash(self, completion):
        assert completion.list
