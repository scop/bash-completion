import pytest


class TestSyncMembers(object):

    @pytest.mark.complete("sync_members --")
    def test_1(self, completion):
        assert completion.list
