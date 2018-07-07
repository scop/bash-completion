import pytest


class TestLdapdelete(object):

    @pytest.mark.complete("ldapdelete -")
    def test_1(self, completion):
        assert completion.list
