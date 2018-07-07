import pytest


class TestListMembers(object):

    @pytest.mark.complete("list_members -")
    def test_1(self, completion):
        assert completion.list
