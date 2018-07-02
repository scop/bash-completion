import pytest


class Test(object):

    @pytest.mark.complete("lusermod ")
    def test_(self, completion):
        assert completion.list
