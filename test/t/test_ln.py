import pytest


class Test(object):

    @pytest.mark.complete("ln ")
    def test_(self, completion):
        assert completion.list
