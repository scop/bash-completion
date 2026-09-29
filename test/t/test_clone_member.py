import pytest


class TestCloneMember:
    @pytest.mark.complete("clone_member -")
    def test_1(self, completion):
        assert completion
