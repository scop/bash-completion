import pytest


class Test(object):

    @pytest.mark.complete("msynctool ")
    def test_(self, completion):
        assert completion.list
