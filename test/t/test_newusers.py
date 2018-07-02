import pytest


class Test(object):

    @pytest.mark.complete("newusers ")
    def test_(self, completion):
        assert completion.list
