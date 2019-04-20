import pytest


class TestLdapmodrdn:
    @pytest.mark.complete("ldapmodrdn -")
    def test_1(self, completion):
        assert completion
