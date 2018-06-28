import pytest


class Test(object):

    @pytest.mark.complete("texindex --")
    def test_dash(self, completion):
        assert completion.list
