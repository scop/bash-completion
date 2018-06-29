import pytest


class Test(object):

    @pytest.mark.complete("smbtree -")
    def test_dash(self, completion):
        assert completion.list
