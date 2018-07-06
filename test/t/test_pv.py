import pytest


class Test(object):

    @pytest.mark.complete("pv ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("pv -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("pv --pidfile ")
    def test_pidfile(self, completion):
        assert completion.list
