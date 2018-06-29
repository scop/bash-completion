import pytest


class Test(object):

    @pytest.mark.complete("quotacheck -")
    def test_dash(self, completion):
        assert completion.list
