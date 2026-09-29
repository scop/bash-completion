import pytest


class TestLdapcompare:
    @pytest.mark.complete("ldapcompare -")
    def test_1(self, completion):
        assert completion
