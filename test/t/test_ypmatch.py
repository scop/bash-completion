import pytest


class Test(object):

    @pytest.mark.complete("ypmatch foo ")
    def test_(self, completion):
        assert completion.list
