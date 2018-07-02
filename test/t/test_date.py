import pytest


class Test(object):

    @pytest.mark.complete("date ")
    def test_(self, completion):
        assert completion.list
