import pytest


class TestRemoveMembers:
    @pytest.mark.complete("remove_members --")
    def test_1(self, completion):
        assert completion
