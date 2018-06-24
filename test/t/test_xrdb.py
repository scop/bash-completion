import pytest


class Test(object):

    @pytest.mark.complete("xrdb ")
    def test_(self, completion):
        assert completion.list
