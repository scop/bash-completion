import pytest


class TestCheckPerms(object):

    @pytest.mark.complete("check_perms -")
    def test_1(self, completion):
        assert completion.list
