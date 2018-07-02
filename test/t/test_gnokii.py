import pytest


class Test(object):

    @pytest.mark.complete("gnokii ")
    def test_(self, completion):
        assert completion.list
