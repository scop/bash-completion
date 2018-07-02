import pytest


class Test(object):

    @pytest.mark.complete("iwpriv --")
    def test_dash(self, completion):
        assert completion.list
