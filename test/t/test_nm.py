import pytest


class Test(object):

    @pytest.mark.complete("nm ")
    def test_(self, completion):
        assert completion.list
