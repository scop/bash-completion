import pytest


class TestSyncMembers:
    @pytest.mark.complete("sync_members --")
    def test_1(self, completion):
        assert completion
