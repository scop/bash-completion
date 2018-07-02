import pytest


class Test(object):

    @pytest.mark.complete("autorpm ")
    def test_(self, completion):
        assert completion.list
