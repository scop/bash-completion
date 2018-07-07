import pytest


class TestListLists(object):

    @pytest.mark.complete("list_lists -")
    def test_1(self, completion):
        assert completion.list
