import pytest


class Test(object):

    @pytest.mark.complete("svnadmin ")
    def test_(self, completion):
        assert completion.list
