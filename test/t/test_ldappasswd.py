import pytest


class TestLdappasswd:
    @pytest.mark.complete("ldappasswd -")
    def test_1(self, completion):
        assert completion
