import pytest


class Test(object):

    @pytest.mark.complete("uscan -")
    def test_dash(self, completion):
        assert completion.list
