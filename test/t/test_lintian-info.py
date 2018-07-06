import pytest


class Test(object):

    @pytest.mark.complete("lintian-info ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("lintian-info --")
    def test_dash(self, completion):
        assert completion.list
