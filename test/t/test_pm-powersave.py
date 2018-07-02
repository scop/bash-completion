import pytest


class Test(object):

    @pytest.mark.complete("pm-powersave ")
    def test_(self, completion):
        assert completion.list
