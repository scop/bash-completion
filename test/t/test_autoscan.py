import pytest


class TestAutoscan(object):

    @pytest.mark.complete("autoscan ")
    def test_1(self, completion):
        assert completion.list
