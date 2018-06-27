import pytest


class Test(object):

    @pytest.mark.complete("vdir ")
    def test_(self, completion):
        assert completion.list
