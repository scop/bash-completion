import pytest


class Test(object):

    @pytest.mark.complete("svk ")
    def test_(self, completion):
        assert completion.list
