import pytest


class Test(object):

    @pytest.mark.complete("brctl ")
    def test_(self, completion):
        assert completion.list
