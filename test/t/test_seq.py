import pytest


class Test(object):

    @pytest.mark.complete("seq --")
    def test_dash(self, completion):
        assert completion.list
