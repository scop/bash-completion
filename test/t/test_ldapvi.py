import pytest


class TestLdapvi:
    @pytest.mark.complete("ldapvi -")
    def test_1(self, completion):
        assert completion
