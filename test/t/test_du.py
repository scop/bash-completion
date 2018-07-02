import pytest


class Test(object):

    @pytest.mark.complete("du ")
    def test_(self, completion):
        assert completion.list
