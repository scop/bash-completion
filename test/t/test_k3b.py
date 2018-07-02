import pytest


class Test(object):

    @pytest.mark.complete("k3b ")
    def test_(self, completion):
        assert completion.list
