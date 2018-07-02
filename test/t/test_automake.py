import pytest


class Test(object):

    @pytest.mark.complete("automake ")
    def test_(self, completion):
        assert completion.list
