import pytest


class Test(object):

    @pytest.mark.complete("iwlist --")
    def test_dash(self, completion):
        assert completion.list
