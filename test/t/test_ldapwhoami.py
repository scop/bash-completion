import pytest


class TestLdapwhoami(object):

    @pytest.mark.complete("ldapwhoami -")
    def test_1(self, completion):
        assert completion.list
