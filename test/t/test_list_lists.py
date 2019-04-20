import pytest


class TestListLists:
    @pytest.mark.complete("list_lists -")
    def test_1(self, completion):
        assert completion
