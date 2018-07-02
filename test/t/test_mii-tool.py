import pytest


class Test(object):

    @pytest.mark.complete("mii-tool ")
    def test_(self, completion):
        assert completion.list
