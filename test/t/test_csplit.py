import pytest


class Test(object):

    @pytest.mark.complete("csplit ")
    def test_(self, completion):
        assert completion.list
