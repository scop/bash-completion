import pytest


class Test(object):

    @pytest.mark.complete("pack200 ")
    def test_(self, completion):
        assert completion.list
