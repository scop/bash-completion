import pytest


class Test(object):

    @pytest.mark.complete("slackpkg -")
    def test_dash(self, completion):
        assert completion.list
