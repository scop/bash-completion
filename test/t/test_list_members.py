import pytest


class TestListMembers:
    @pytest.mark.complete("list_members -")
    def test_1(self, completion):
        assert completion
