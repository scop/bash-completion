import pytest


class Test(object):

    @pytest.mark.complete("json_xs ")
    def test_(self, completion):
        assert not completion.list

    @pytest.mark.complete("json_xs -")
    def test_dash(self, completion):
        assert completion.list
