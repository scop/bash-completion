import pytest


class Test(object):

    @pytest.mark.complete("autoreconf ")
    def test_(self, completion):
        assert completion.list
