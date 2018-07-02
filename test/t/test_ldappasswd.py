import pytest


class Test(object):

    @pytest.mark.complete("ldappasswd -")
    def test_dash(self, completion):
        assert completion.list
