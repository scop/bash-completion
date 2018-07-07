import pytest


class TestRemoveMembers(object):

    @pytest.mark.complete("remove_members --")
    def test_1(self, completion):
        assert completion.list
