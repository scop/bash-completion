import pytest


class Test(object):

    @pytest.mark.complete("autoheader ")
    def test_(self, completion):
        assert completion.list
