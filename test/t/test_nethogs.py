import pytest


class Test(object):

    @pytest.mark.complete("nethogs ")
    def test_(self, completion):
        assert completion.list
