import pytest


class Test(object):

    @pytest.mark.complete("kldload ")
    def test_(self, completion):
        assert completion.list
