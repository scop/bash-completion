import pytest


class Test(object):

    @pytest.mark.complete("rlog ")
    def test_(self, completion):
        assert completion.list
