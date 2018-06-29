import pytest


class Test(object):

    @pytest.mark.complete("rfcomm ")
    def test_(self, completion):
        assert completion.list
