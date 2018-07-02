import pytest


class Test(object):

    @pytest.mark.complete("mussh -")
    def test_dash(self, completion):
        assert completion.list
