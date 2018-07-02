import pytest


class Test(object):

    @pytest.mark.complete("mc -")
    def test_dash(self, completion):
        assert completion.list
