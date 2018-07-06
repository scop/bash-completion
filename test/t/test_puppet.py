import pytest


class Test(object):

    @pytest.mark.complete("puppet ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("puppet agent --")
    def test_agent_(self, completion):
        assert completion.list
