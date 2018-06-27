import pytest


class Test(object):

    @pytest.mark.complete("xsltproc ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xsltproc -")
    def test_dash(self, completion):
        assert completion.list
