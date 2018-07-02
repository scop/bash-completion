import pytest


class Test(object):

    @pytest.mark.complete("lintian --")
    def test_dash(self, completion):
        assert completion.list
