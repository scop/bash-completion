import pytest


class Test(object):

    @pytest.mark.complete("rcs ")
    def test_(self, completion):
        assert completion.list
