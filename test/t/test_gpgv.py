import pytest


class Test(object):

    @pytest.mark.complete("gpgv ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("gpgv -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("gpgv foo.sig foo ")
    def test_3rdarg(self, completion):
        assert not completion.list
