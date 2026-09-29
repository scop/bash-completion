import pytest


class TestLdapdelete:
    @pytest.mark.complete("ldapdelete -")
    def test_1(self, completion):
        assert completion
