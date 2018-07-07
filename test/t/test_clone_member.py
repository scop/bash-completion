import pytest


class TestCloneMember(object):

    @pytest.mark.complete("clone_member -")
    def test_1(self, completion):
        assert completion.list
