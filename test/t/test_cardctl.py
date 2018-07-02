import pytest


class Test(object):

    @pytest.mark.complete("cardctl ")
    def test_(self, completion):
        assert completion.list
