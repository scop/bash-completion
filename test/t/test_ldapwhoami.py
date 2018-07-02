import pytest


class Test(object):

    @pytest.mark.complete("ldapwhoami -")
    def test_dash(self, completion):
        assert completion.list
