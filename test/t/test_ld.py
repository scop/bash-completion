import pytest


class Test(object):

    @pytest.mark.complete("ld ")
    def test_(self, completion):
        assert completion.list
