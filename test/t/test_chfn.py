import pytest


class Test(object):

    @pytest.mark.complete("chfn ")
    def test_(self, completion):
        assert completion.list
