import pytest


class Test(object):

    @pytest.mark.complete("hping2 ")
    def test_(self, completion):
        assert completion.list
