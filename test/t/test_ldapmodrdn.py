import pytest


class Test(object):

    @pytest.mark.complete("ldapmodrdn -")
    def test_dash(self, completion):
        assert completion.list
