import pytest


class TestLdapwhoami:
    @pytest.mark.complete("ldapwhoami -")
    def test_1(self, completion):
        assert completion
