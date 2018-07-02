import pytest


class Test(object):

    @pytest.mark.complete("e2freefrag ")
    def test_(self, completion):
        assert completion.list
