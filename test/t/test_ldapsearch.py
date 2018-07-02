import pytest


class Test(object):

    @pytest.mark.complete("ldapsearch -")
    def test_dash(self, completion):
        assert completion.list
