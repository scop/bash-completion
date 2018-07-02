import pytest


class Test(object):

    @pytest.mark.complete("postmap ")
    def test_(self, completion):
        assert completion.list
