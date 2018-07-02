import pytest


class Test(object):

    @pytest.mark.complete("df ")
    def test_(self, completion):
        assert completion.list
