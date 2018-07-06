import pytest


class Test(object):

    @pytest.mark.complete("mcrypt ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("mcrypt -a ")
    def test_a(self, completion):
        assert completion.list

    @pytest.mark.complete("mcrypt -m ")
    def test_m(self, completion):
        assert completion.list
