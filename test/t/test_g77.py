import pytest


class TestG77(object):

    @pytest.mark.complete("g77 ")
    def test_1(self, completion):
        assert completion.list
