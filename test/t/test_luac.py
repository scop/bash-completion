import pytest


class Test(object):

    @pytest.mark.complete("luac ")
    def test_(self, completion):
        assert completion.list
