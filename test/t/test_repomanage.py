import pytest


class Test(object):

    @pytest.mark.complete("repomanage ")
    def test_(self, completion):
        assert completion.list
