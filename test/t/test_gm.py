import pytest


class Test(object):

    @pytest.mark.complete("gm ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("gm help ")
    def test_help(self, completion):
        assert completion.list

    @pytest.mark.complete("gm time ")
    def test_time(self, completion):
        assert completion.list

    @pytest.mark.complete("gm version ")
    def test_version(self, completion):
        assert not completion.list
