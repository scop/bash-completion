import pytest


class Test(object):

    @pytest.mark.complete("unpack200 ")
    def test_(self, completion):
        assert completion.list
