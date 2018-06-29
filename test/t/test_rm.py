import pytest


class Test(object):

    @pytest.mark.complete("rm ")
    def test_(self, completion):
        assert completion.list
