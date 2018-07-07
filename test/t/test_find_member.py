import pytest


class TestFindMember(object):

    @pytest.mark.complete("find_member -")
    def test_1(self, completion):
        assert completion.list
