import pytest


class Test(object):

    @pytest.mark.complete("g++ ")
    def test_(self, completion):
        assert completion.list
