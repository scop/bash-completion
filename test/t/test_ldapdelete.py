import pytest


class Test(object):

    @pytest.mark.complete("ldapdelete -")
    def test_dash(self, completion):
        assert completion.list
