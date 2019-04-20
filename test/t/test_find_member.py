import pytest


class TestFindMember:
    @pytest.mark.complete("find_member -")
    def test_1(self, completion):
        assert completion
