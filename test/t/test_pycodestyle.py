import pytest


class Test(object):

    @pytest.mark.complete("pycodestyle ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("pycodestyle -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("pycodestyle --doesnt-exist=")
    def test_doesnt_exist(self, completion):
        assert not completion.list
