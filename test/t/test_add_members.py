import pytest


class TestAddMembers:
    @pytest.mark.complete("add_members -")
    def test_1(self, completion):
        assert completion
