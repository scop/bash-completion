import pytest


class Test(object):

    @pytest.mark.complete("genisoimage ")
    def test_(self, completion):
        assert completion.list
