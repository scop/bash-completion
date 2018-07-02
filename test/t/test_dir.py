import pytest


class Test(object):

    @pytest.mark.complete("dir ")
    def test_(self, completion):
        assert completion.list
