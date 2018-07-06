import pytest


class Test(object):

    @pytest.mark.complete("perltidy ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("perltidy -h")
    def test_h(self, completion):
        assert completion.list

    @pytest.mark.complete("perltidy -ole=")
    def test_ole(self, completion):
        assert completion.list

    @pytest.mark.complete("perltidy -doesntexist=")
    def test_doesntexist(self, completion):
        assert not completion.list
