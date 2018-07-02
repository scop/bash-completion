import pytest


class Test(object):

    @pytest.mark.complete("less --")
    def test_dash(self, completion):
        assert completion.list
