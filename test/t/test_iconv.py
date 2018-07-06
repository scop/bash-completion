import pytest


class Test(object):

    @pytest.mark.complete("iconv -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("iconv -f UTF")
    def test_f(self, completion):
        assert completion.list
