import pytest


class TestLdappasswd(object):

    @pytest.mark.complete("ldappasswd -")
    def test_1(self, completion):
        assert completion.list
