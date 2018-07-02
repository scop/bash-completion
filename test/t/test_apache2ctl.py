import pytest


class Test(object):

    @pytest.mark.complete("apache2ctl ")
    def test_(self, completion):
        assert completion.list
