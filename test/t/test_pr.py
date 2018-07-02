import pytest


class Test(object):

    @pytest.mark.complete("pr ")
    def test_(self, completion):
        assert completion.list
