import pytest


class TestLdapmodrdn(object):

    @pytest.mark.complete("ldapmodrdn -")
    def test_1(self, completion):
        assert completion.list
