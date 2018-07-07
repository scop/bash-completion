import pytest


class TestAddMembers(object):

    @pytest.mark.complete("add_members -")
    def test_1(self, completion):
        assert completion.list
