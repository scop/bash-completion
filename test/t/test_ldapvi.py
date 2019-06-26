import pytest


class TestLdapvi:
    @pytest.mark.complete("ldapvi -", require_cmd=True)
    def test_1(self, completion):
        assert completion
