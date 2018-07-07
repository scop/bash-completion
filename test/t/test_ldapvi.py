import pytest


class TestLdapvi(object):

    @pytest.mark.complete("ldapvi -")
    def test_1(self, completion):
        assert completion.list
