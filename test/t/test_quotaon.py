import pytest


class Test(object):

    @pytest.mark.complete("quotaon -")
    def test_dash(self, completion):
        assert completion.list
