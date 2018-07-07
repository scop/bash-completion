import pytest


class TestTexindex(object):

    @pytest.mark.complete("texindex --")
    def test_1(self, completion):
        assert completion.list
