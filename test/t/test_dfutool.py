import pytest


class Test(object):

    @pytest.mark.complete("dfutool ")
    def test_(self, completion):
        assert completion.list
