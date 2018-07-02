import pytest


class Test(object):

    @pytest.mark.complete("ldapcompare -")
    def test_dash(self, completion):
        assert completion.list
