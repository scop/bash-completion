import pytest


class Test(object):

    @pytest.mark.complete("diff --")
    def test_dash(self, completion):
        assert completion.list
