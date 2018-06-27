import pytest


class Test(object):

    @pytest.mark.complete("xmllint ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xmllint -")
    def test_dash(self, completion):
        assert completion.list
