import pytest


class Test(object):

    @pytest.mark.complete("newlist -")
    def test_dash(self, completion):
        assert completion.list
