import pytest


class Test(object):

    @pytest.mark.complete("rmlist -")
    def test_dash(self, completion):
        assert completion.list
