import pytest


class TestListAdmins(object):

    @pytest.mark.complete("list_admins -")
    def test_1(self, completion):
        assert completion.list
