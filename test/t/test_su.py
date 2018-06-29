import pytest


class Test(object):

    @pytest.mark.complete("su ")
    def test_(self, completion):
        assert completion.list
