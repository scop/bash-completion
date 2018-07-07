import pytest


class TestLdapcompare(object):

    @pytest.mark.complete("ldapcompare -")
    def test_1(self, completion):
        assert completion.list
