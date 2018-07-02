import pytest


class Test(object):

    @pytest.mark.complete("ether-wake ")
    def test_(self, completion):
        assert completion.list
