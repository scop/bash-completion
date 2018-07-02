import pytest


class Test(object):

    @pytest.mark.complete("a2x ")
    def test_(self, completion):
        assert completion.list
